"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79$g*#82qs_rl%3vmdand$g6#n%u9#w6c6$(-np%p@p3a2rhu!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Django Uygulamaları
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Kendi Uygulamarım
    'post',
    # 3. Parti Uygulamalar
    'crispy_forms',
    'django_cleanup',
    'ckeditor',
    'blog',
    'django.contrib.sites',
    # "crispy_bootstrap5",
    'storages',
    'upload',
    'easy_thumbnails',





]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# FILER_CANONICAL_URL = 'sharing/'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #
    # 'django_reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# print(os.path.join(BASE_DIR, 'db.sqlite3'))

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Minio credentials and bucket name
AWS_ACCESS_KEY_ID = '*'
AWS_SECRET_ACCESS_KEY = '*'
AWS_STORAGE_BUCKET_NAME = '*'

# Storage settings
AWS_S3_ENDPOINT_URL = '/*/'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

# s3 static settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/static/"
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# s3 media settings
DEFAULT_FILE_STORAGE = 'blog.storages.MediaStorage'
# DEFAULT_FILE_STORAGE = 'post.views.upload_file_to_minio'
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'js/jquery.min.js')
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    },
}