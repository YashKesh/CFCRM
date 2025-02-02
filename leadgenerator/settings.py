"""
Django settings for leadgenerator project.
Generated by 'django-admin startproject' using Django 3.1.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from json import load
import os
from pathlib import Path
import django_heroku
from django.contrib.messages import constants as messages
# https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
import environ
from dotenv import load_dotenv
# Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
MEDIA_DIR = BASE_DIR / 'media'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
# print("There", os.environ.get('SECRET_KEY'))
# SECRET_KEY = os.environ.get("SECRET_KEY")
#SECRET_KEY = "abcdefghijklmn"
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = [env('ALLOWED_HOST_1'), env('ALLOWED_HOST_2')]
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'master.apps.MasterConfig',
    'HomeLoan.apps.HomeloanConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'stronghold',
    'mathfilters'
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
    'stronghold.middleware.LoginRequiredMiddleware',
]


ROOT_URLCONF = 'leadgenerator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'leadgenerator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'init_command': "SET sql_mode=STRICT_TRANS_TABLES",
        },
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'creativefinserve$leadgen',
        # 'NAME': os.environ.get('DATABASES_NAME'),
        'NAME': os.getenv('DATABASES_NAME'),
        # 'USER': 'creativefinserve',
        # 'USER': os.environ.get('DATABASES_USER'),
        'USER': os.getenv('DATABASES_USER'),
        # 'PASSWORD': '_HP@B99_',
        'PASSWORD': os.getenv('DATABASES_PASS'),
        # 'HOST': 'creativefinservecrm.mysql.pythonanywhere-services.com',
        # 'HOST': os.environ.get('DATABASES_HOST'),
        'HOST': os.getenv('DATABASES_HOST'),
        # 'PORT': os.environ.get('DATABASES_PORT'),
        'PORT': os.getenv('DATABASES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'account.CustomUser'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR / 'documents'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# SMTP Configuration
# EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_PORT = 587
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_USER = 'rajsingh08471@gmail.com'
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = 'rzvujwqswaduhgih'

django_heroku.settings(locals())

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

LOGIN_URL = '/account/login'

# https://github.com/mgrouchy/django-stronghold
# STRONGHOLD_DEFAULTS = env('STRONGHOLD_DEFAULTS')
STRONGHOLD_PUBLIC_NAMED_URLS = ('home', 'register', 'forgot_username', 'reset_password',
                                'password_reset_done', 'password_reset_confirm', 'password_reset_complete', )
STRONGHOLD_PUBLIC_URLS = ('/admin/',)
