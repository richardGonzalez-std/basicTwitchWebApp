from django.shortcuts import render
from basicTwitchWebApp import settings
from django.shortcuts import redirect
import requests
# Create your views here.
def index(request):
    is_logged = 'twitch_access_token' in request.session
    if is_logged:
        user_data = requests.get("https://api.twitch.tv/helix/users",headers={
            "Authorization": f"Bearer {request.session['twitch_access_token']}",
            "Client-Id": settings.CLIENT_ID
        })
        follow_data = requests.get(f"https://api.twitch.tv/helix/streams/followed?user_id={user_data.json()['data'][0]['id']}",headers={
            "Authorization": f"Bearer {request.session['twitch_access_token']}",
            "Client-Id": settings.CLIENT_ID
        }).json()
        img_url_set = []
        for url in follow_data['data']:
            if url["thumbnail_url"] not in img_url_set:
                url['thumbnail_url'] = url["thumbnail_url"].replace("{width}","500").replace("{height}","350")
                img_url_set.append(url["thumbnail_url"])
        combined_data = zip(follow_data['data'], img_url_set)
        return render(request,"twitchApp/index.html",{ "logged":True, "client_id":settings.CLIENT_ID,"access_token":request.session['twitch_access_token'],'user_data':user_data.json() ,"combined_data":list(combined_data)})
    return render(request,"twitchApp/index.html",{ "logged":False, "client_id":settings.CLIENT_ID,"redirect_uri":settings.REDIRECT_URI})

def validate(request):
    code = request.GET.get('code')
    token_data = requests.post("https://id.twitch.tv/oauth2/token",data={
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": settings.REDIRECT_URI
    })
    token_data.raise_for_status()
    token_json = token_data.json()
    print(token_json)
    access_token = token_json["access_token"]
    if access_token:
        print("Access token obtained:", access_token)
        request.session['twitch_access_token'] = access_token
        return redirect("index")
    
def logout(request):
    if 'twitch_access_token' in request.session:
        del request.session['twitch_access_token']
    return redirect("index")