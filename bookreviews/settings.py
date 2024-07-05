"""
Django settings for bookreviews project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from environs import Env
from pathlib import Path
import os
# import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#Environments variable 
env = Env()
env.read_env()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "rest_framework",
    #app
    'accounts',
    'pages',
    'books',
    "apis.apps.ApisConfig",
    
    "debug_toolbar",
    "crispy_forms", # new
    "crispy_bootstrap5", # new
    "allauth", # new
    "allauth.account", #
    

]
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", # new
)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" # new
CRISPY_TEMPLATE_PACK = "bootstrap5" #

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"
AUTH_USER_MODEL = "accounts.CustomUser"
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ""
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = "bookreviews.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'books.context_processors.genres',
            ],
        },
    },
]

WSGI_APPLICATION = "bookreviews.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookdb',
        'USER': 'apple',
        'PASSWORD': 'wCh29&HE&T83',
        'HOST': '127.0.0.1',
        # 'PORT': '5342',
    }
    
}
# DATABASES = {
#     "default": env.dj_db_url('DATABASE_URL',default = 'sqlite://db.sqlite3')
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "/media/" # new
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = "email" # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True