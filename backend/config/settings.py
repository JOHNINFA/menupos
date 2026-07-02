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
# BASE DE DATOS
# ============================================
# Decisión de FASE 2: usamos SQLite (un solo archivo, cero configuración)
# para desarrollar rápido sin depender de Docker/PostgreSQL todavía.
#
# Migraremos a PostgreSQL en una fase dedicada más adelante (cuando
# preparemos Docker Compose), porque en producción SIEMPRE se usa
# un motor de base de datos real, no SQLite.
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

# MEDIA = archivos que SUBEN los usuarios (ej: fotos de productos).
# En desarrollo se guardan localmente; en FASE 8 los moveremos a AWS S3.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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
