"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

import dj_database_url
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(os.path.join(BASE_DIR, 'env/.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='foo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=0)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'obscure-sands-56196.herokuapp.com',
                 'https://obscure-sands-56196.herokuapp.com']
INTERNAL_IPS = ALLOWED_HOSTS

# Application definition

INSTALLED_APPS = [
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    "crispy_forms",
    "crispy_bootstrap5",

    # local
    'home.apps.HomeConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""
Local development database settings. 
"""
# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
#         'NAME': os.environ.get('POSTGRES_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
#         'USER': os.environ.get('POSTGRES_USER', 'user'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

"""
Heroku and docker database settings. Uncomment when you want to use it.
"""

DATABASES_URL = os.environ.get('DATABASE_URL')
# dj-database-url paczka do podpinania database
db_from_env = dj_database_url.config(
    default=DATABASES_URL, conn_max_age=500, ssl_require=False,
)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    # os.path.join(BASE_DIR, 'venv/lib64/python3.8/site-packages/highcharts')
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "landing"

LOGOUT_REDIRECT_URL = 'landing'

CSRF_TRUSTED_ORIGINS = ('https://obscure-sands-56196.herokuapp.com', 'http://0.0.0.0:8000', 'http://127.0.0.1/')

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
