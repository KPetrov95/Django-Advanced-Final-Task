"""
Django settings for bookStore project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from decouple import config
from django.core.files import images
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', config('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', config('DEBUG')) == "True"

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', config('ALLOWED_HOSTS', default='')).split(',')

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', config('CSRF_TRUSTED_ORIGINS', [])).split(',')


# Application definition

MY_APPS = [
    "bookStore.catalog.apps.CatalogConfig",
    "bookStore.accounts.apps.AccountsConfig",
    "bookStore.common",
    "bookStore.orders",
]

INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',

                     'rest_framework',
                     'tailwind',
                     'theme',
                     'django_browser_reload',
                     'cloudinary',
                     'cloudinary_storage',

                 ] + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += [
        'django_browser_reload.middleware.BrowserReloadMiddleware',
    ]

ROOT_URLCONF = 'bookStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'bookStore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME', config('DB_NAME')),
        "USER": os.getenv('DB_USER', config('DB_USER')),
        "PASSWORD": os.getenv('DB_PASSWORD', config('DB_PASSWORD')),
        "HOST": os.getenv('DB_HOST', config('DB_HOST')),
        "PORT": os.getenv('DB_PORT', config('DB_PORT')),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', config('CELERY_BROKER_URL'))
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = 'C:\\Program Files\\nodejs\\npm.cmd'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_NAME', config('CLOUDINARY_NAME')),
    api_key=os.getenv('CLOUDINARY_API_KEY', config('CLOUDINARY_API_KEY')),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', config('CLOUDINARY_API_SECRET')),
    secure=True
)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_NAME', config('CLOUDINARY_NAME')),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', config('CLOUDINARY_API_KEY')),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', config('CLOUDINARY_API_SECRET')),
}

AUTH_USER_MODEL = 'accounts.AppUser'
LOGIN_REDIRECT_URL = reverse_lazy('book_list')
LOGOUT_REDIRECT_URL = reverse_lazy('login')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', config('EMAIL_HOST'))
EMAIL_PORT = os.getenv('EMAIL_PORT', config('EMAIL_PORT'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', config('EMAIL_USE_TLS')) == "True"
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', config('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', config('EMAIL_HOST_PASSWORD'))
