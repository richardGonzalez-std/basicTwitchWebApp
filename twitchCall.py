import requests
import json
apiCall = requests.get('https://api.twitch.tv/helix/users?login=Rubius', headers={
    'Authorization':'Bearer 8jcmcwvoumw27g67gs2n9vmt5tf85g',
    'Client-Id': 'i4dllv4q6b9dpt2mglwbaw0gfz8139',
}).content

apiJson = json.loads(apiCall)

id = apiJson['data'][0]['id']
username = apiJson['data'][0]['login']
