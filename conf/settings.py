import os
from pathlib import Path
from dotenv import load_dotenv
import mongoengine

# Carga las variables de entorno del archivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-hx(_j@_4&^27t3s(*ud0l-@fqm_bmk1crg!i&+)*+0q#kka#6u"

DEBUG = False

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.onrender.com', '.railway.app']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.incidentes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conf.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


MONGO_SETTINGS = {
    "HOST": os.environ.get("MONGO_HOST"),
    "PORT": int(os.environ.get("MONGO_PORT", 27017)),
    "DB_NAME": os.environ.get("MONGO_DB_NAME"),
    "USER": os.environ.get("MONGO_USER", "admin"),
    "PASSWORD": os.environ.get("MONGO_PASS", ""),
}

mongoengine.connect(
    db=MONGO_SETTINGS["DB_NAME"],
    host=MONGO_SETTINGS["HOST"],
    port=MONGO_SETTINGS["PORT"],
    username=MONGO_SETTINGS["USER"],
    password=MONGO_SETTINGS["PASSWORD"],
    authentication_source=MONGO_SETTINGS["DB_NAME"],
)

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

LANGUAGE_CODE = "es-cl"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_DIRS = []
