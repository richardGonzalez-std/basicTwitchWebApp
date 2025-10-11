# 🎮 Twitch Streams Viewer

Una aplicación web Django que permite a los usuarios autenticarse con Twitch y ver los streams en vivo de los canales que siguen.

![Screenshot](/screenshot/screenshot_1.png) <!-- Agrega una captura de pantalla -->
![Screenshot](/screenshot/screenshot_2.png) <!-- Agrega una captura de pantalla -->

## ✨ Características

- 🔐 Autenticación OAuth 2.0 con Twitch
- 📺 Visualización de streams en vivo de canales seguidos
- 🎥 Reproductor Twitch embebido en modal
- 📊 Información en tiempo real (viewers, categoría)
- 🎨 Interfaz moderna y responsive con Bootstrap 5

## 🛠️ Tecnologías

- **Backend**: Django 4.2, Python 3.x
- **Frontend**: HTML5, Bootstrap 5, JavaScript (Vanilla)
- **API**: Twitch API (Helix)
- **Autenticación**: OAuth 2.0

## 📋 Requisitos Previos

- Python 3.8+
- Cuenta de desarrollador en [Twitch](https://dev.twitch.tv/)
- pip

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/twitch-viewer.git
cd twitch-viewer
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install django python-decouple requests
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=tu-secret-key-django
DEBUG=True
CLIENT_ID=tu-twitch-client-id
CLIENT_SECRET=tu-twitch-client-secret
REDIRECT_URI=http://localhost:8000/validate/
```

**Para obtener credenciales de Twitch:**
1. Ve a [Twitch Developer Console](https://dev.twitch.tv/console)
2. Crea una nueva aplicación
3. Añade `http://localhost:8000/validate/` como OAuth Redirect URL
4. Copia el Client ID y Client Secret

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Iniciar servidor
```bash
python manage.py runserver
```

Visita `http://localhost:8000`

## 📱 Uso

1. Haz clic en "Login con Twitch"
2. Autoriza la aplicación
3. Verás los streams en vivo de los canales que sigues
4. Haz clic en cualquier card para ver el stream en el reproductor embebido

## 🏗️ Estructura del Proyecto

```
basicTwitchWebApp/
├── basicTwitchWebApp/      # Configuración principal
│   ├── settings.py
│   └── urls.py
├── twitchApp/              # App Django
│   ├── templates/
│   │   └── twitchApp/
│   │       └── index.html
│   ├── views.py
│   └── urls.py
└── manage.py
```

## 🔒 Seguridad

- Las credenciales están protegidas mediante variables de entorno
- El archivo `.env` está en `.gitignore`
- OAuth 2.0 para autenticación segura

## 🎯 Funcionalidades Futuras

- [ ] Refresh token implementation
- [ ] Búsqueda de streams por categoría
- [ ] Sistema de favoritos
- [ ] Notificaciones cuando un streamer va en vivo
- [ ] Chat en vivo integrado
- [ ] Historial de visualización

## 🤝 Contribuciones

Este es un proyecto de portafolio personal, pero sugerencias son bienvenidas.

## 📄 Licencia

MIT License

## 👤 Autor

**Tu Nombre**
- GitHub: [@richardGonzalez-std](https://github.com/richardGonzalez-std)
- LinkedIn: [riparedesgonzalez](www.linkedin.com/in/riparedesgonzalez)

## 🙏 Agradecimientos

- [Twitch API Documentation](https://dev.twitch.tv/docs/api/)
- [Django Documentation](https://docs.djangoproject.com/)
