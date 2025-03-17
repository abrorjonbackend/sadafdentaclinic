import os
from pathlib import Path

# Bazaviy papka yo'li
BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsiz kalit
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "super-secret-key")

# DEBUG rejimi
DEBUG = os.getenv("DEBUG", "True") == "True"

# Ruxsat berilgan domenlar
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "sadafdentaclinic.uz",
    "www.sadafdentaclinic.uz"
]

# Django ilovalari
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",  # DRF
    "corsheaders",  # CORS ruxsati
    "myapp",  # O'zingizning ilovangizni qo'shing
]

# Middleware (CORS va boshqalar)
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS Middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL konfiguratsiya
ROOT_URLCONF = "myproject.urls"

# Django REST Framework sozlamalari
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Hamma foydalanishi uchun
    ],
}

# CORS sozlamalari
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://sadafdentaclinic.uz",
    "https://www.sadafdentaclinic.uz"
]
CORS_ALLOW_CREDENTIALS = True

# Templateni sozlash
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI sozlamasi
WSGI_APPLICATION = ("myproject"
                    ".wsgi.application")

# Ma'lumotlar bazasi (agar PostgreSQL ishlatsangiz, sozlash kerak)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Agar PostgreSQL ishlatsangiz: "django.db.backends.postgresql"
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Parol sozlamalari
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Til va vaqtni sozlash
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# Static va Media fayllar
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default birlamchi kalit
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
