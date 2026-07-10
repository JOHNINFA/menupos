"""
Configuración central de Django para MenuPOS.

Analogía: este archivo es como el "tablero de control" del restaurante.
Aquí se decide: qué apps existen, cómo se conecta a la BD, quién puede
entrar (CORS), cómo funciona el login (JWT), etc.

Ver la mini-clase: docs/clases/02-django-venv-dependencias.md
"""

from pathlib import Path
from datetime import timedelta
from decouple import config
import dj_database_url

# BASE_DIR = la carpeta raíz del backend (donde está manage.py).
# Se usa para construir rutas relativas sin importar en qué compu corra.
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================
# SEGURIDAD BÁSICA
# ============================================
# SECRET_KEY: se usa para encriptar sesiones, tokens CSRF, etc.
# NUNCA se debe subir a Git ni compartir. Por eso la leemos desde
# el archivo .env (que está en .gitignore) usando `decouple.config`.
SECRET_KEY = config('DJANGO_SECRET_KEY', default='clave-insegura-solo-para-desarrollo')

# DEBUG=True muestra errores detallados (útil mientras programamos).
# En producción SIEMPRE debe ser False (si no, expones información sensible).
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)

# Lista de dominios que pueden servir esta app. En desarrollo basta
# con localhost. En producción aquí va el dominio real (ej: menupos.com).
ALLOWED_HOSTS = config(
    'DJANGO_ALLOWED_HOSTS',
    default='localhost,127.0.0.1',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# Cada plataforma de deploy le pone a la app un dominio y lo expone en una
# variable de entorno. Lo agregamos a ALLOWED_HOSTS solo si existe, para
# que en producción Django acepte peticiones a ese dominio sin escribirlo
# a mano. Soportamos Railway y Render.
RAILWAY_PUBLIC_DOMAIN = config('RAILWAY_PUBLIC_DOMAIN', default='')
RENDER_EXTERNAL_HOSTNAME = config('RENDER_EXTERNAL_HOSTNAME', default='')

for dominio in (RAILWAY_PUBLIC_DOMAIN, RENDER_EXTERNAL_HOSTNAME):
    if dominio:
        ALLOWED_HOSTS.append(dominio)


# ============================================
# APLICACIONES INSTALADAS
# ============================================
# Cada string es una "app". Django trae varias por defecto (admin, auth, etc.)
# Nosotros agregamos las nuestras (users, menu, sales) + librerías externas.
INSTALLED_APPS = [
    # --- Apps nativas de Django ---
    'django.contrib.admin',            # Panel de administración web (/admin)
    'django.contrib.auth',             # Sistema de usuarios y permisos
    'django.contrib.contenttypes',     # Requerido por auth y admin
    'django.contrib.sessions',         # Manejo de sesiones
    'django.contrib.messages',         # Mensajes flash (ej: "guardado con éxito")
    'django.contrib.staticfiles',      # Manejo de archivos estáticos (CSS, JS)

    # --- Librerías externas (instaladas via pip) ---
    'rest_framework',                  # Django REST Framework: para crear la API
    'rest_framework_simplejwt',        # Autenticación con tokens JWT
    'corsheaders',                     # Permite que React (otro dominio) llame la API
    'storages',                        # django-storages: para guardar imágenes en S3

    # --- Nuestras apps (el "menú" de secciones de MenuPOS) ---
    'users',   # Usuarios: administrador y mesero
    'menu',    # Categorías y productos del restaurante
    'sales',   # Ventas y detalle de cada venta
]


# ============================================
# MIDDLEWARE
# ============================================
# El middleware es una "cadena de filtros" por la que pasa cada petición
# ANTES de llegar a nuestro código, y cada respuesta ANTES de salir.
# El ORDEN importa: CorsMiddleware debe ir bien arriba, antes de CommonMiddleware.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise sirve los archivos estáticos (CSS/JS del admin de Django)
    # en producción sin necesitar un servidor web aparte. Va justo después
    # de SecurityMiddleware, como pide su documentación.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',        # ← agregado para CORS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# ============================================
# BASE DE DATOS — configuración dual (FASE 8)
# ============================================
# Regla: si existe la variable DATABASE_URL (la pone Railway en producción),
# usamos PostgreSQL; si no existe (tu PC), seguimos con SQLite local.
#
# Así el MISMO código corre con SQLite en desarrollo (cero configuración)
# y con PostgreSQL en producción (robusto, no se borra al redesplegar),
# sin que tengas que instalar Postgres en tu máquina.
DATABASE_URL = config('DATABASE_URL', default='')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ============================================
# VALIDACIÓN DE CONTRASEÑAS
# ============================================
# Reglas que Django aplica automáticamente al crear usuarios,
# para evitar contraseñas débiles (ej: "12345", igual al nombre, etc.)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================
# INTERNACIONALIZACIÓN
# ============================================
LANGUAGE_CODE = 'es'          # Español (por defecto Django trae 'en-us')
TIME_ZONE = 'America/Bogota'  # Zona horaria de Colombia
USE_I18N = True
USE_TZ = True


# ============================================
# ARCHIVOS ESTÁTICOS Y MEDIA
# ============================================
STATIC_URL = 'static/'

# STATIC_ROOT: carpeta donde `collectstatic` junta todos los estáticos
# para que WhiteNoise los sirva en producción. No se usa en desarrollo.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA = archivos que SUBEN los usuarios (ej: fotos de productos).
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---- Almacenamiento de imágenes: local o AWS S3 ----
# USE_S3 es un "interruptor": si está en true Y hay credenciales, las
# imágenes se guardan en un bucket de AWS S3; si no, se guardan en el
# disco local (media/). Así el código funciona igual en ambos modos y
# activar S3 es solo cambiar variables en .env, sin tocar código.
# Ver mini-clase: docs/clases/12-aws-s3.md
USE_S3 = config('USE_S3', default=False, cast=bool)

if USE_S3:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='us-east-1')

    # No sobreescribir un archivo si sube otro con el mismo nombre.
    AWS_S3_FILE_OVERWRITE = False
    # No firmar las URLs (el bucket sirve las imágenes como públicas).
    AWS_QUERYSTRING_AUTH = False

    # STORAGES (Django 5): le decimos que los archivos "default" (los que
    # suben los usuarios, como las fotos de productos) vivan en S3.
    STORAGES = {
        'default': {'BACKEND': 'storages.backends.s3.S3Storage'},
        'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Le decimos a Django que use NUESTRO modelo Usuario (con el campo `rol`)
# en vez del modelo de usuario por defecto. Esto debe declararse ANTES
# de la primera migración de la app 'users' — cambiarlo después de tener
# datos reales es complicado, así que lo definimos desde el inicio.
AUTH_USER_MODEL = 'users.Usuario'


# ============================================
# DJANGO REST FRAMEWORK (DRF)
# ============================================
# Configuración global de cómo se comporta nuestra API.
REST_FRAMEWORK = {
    # Por defecto, TODAS las peticiones deben venir con un token JWT válido.
    # Las vistas públicas (ej: login) se marcan explícitamente como excepción.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# ============================================
# JWT (JSON Web Tokens) — la "pulsera VIP"
# ============================================
# Ver mini-clase 05 (autenticación) cuando lleguemos a esa fase.
SIMPLE_JWT = {
    # El access token dura poco (es la pulsera que usas todo el turno)
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=config('JWT_ACCESS_TOKEN_LIFETIME_MIN', default=60, cast=int)
    ),
    # El refresh token dura más (permite renovar la pulsera sin loguearse de nuevo)
    'REFRESH_TOKEN_LIFETIME': timedelta(
        days=config('JWT_REFRESH_TOKEN_LIFETIME_DAYS', default=7, cast=int)
    ),
}


# ============================================
# CORS (Cross-Origin Resource Sharing)
# ============================================
# El navegador BLOQUEA por seguridad que una web en un dominio (React en
# localhost:5173) llame a una API en OTRO dominio (Django en localhost:8000),
# a menos que el backend diga explícitamente "confío en ese origen".
# Eso es justo lo que configuramos aquí.
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:5173',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# CSRF_TRUSTED_ORIGINS: en producción Django exige declarar los dominios
# (con https://) desde los que se aceptan peticiones que cambian datos.
# Se llena con la URL del frontend en Vercel (ej: https://menupos.vercel.app).
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://localhost:5173',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# También confiamos en el propio dominio de la plataforma (para el admin
# de Django, que sí usa CSRF).
for dominio in (RAILWAY_PUBLIC_DOMAIN, RENDER_EXTERNAL_HOSTNAME):
    if dominio:
        CSRF_TRUSTED_ORIGINS.append(f'https://{dominio}')
