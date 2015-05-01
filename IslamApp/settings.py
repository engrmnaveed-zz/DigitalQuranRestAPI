"""
Django settings for IslamApp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0j7cyv_2@dkdv&65%o0$l6j$xilhe_5_0$oehttk27y)%hb@^r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',              
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'corsheaders',
    'digital_QURAN',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'IslamApp.urls'

WSGI_APPLICATION = 'IslamApp.wsgi.application'

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

CORS_ORIGIN_ALLOW_ALL = True


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 
        'NAME': 'iqradb',
#         'NAME': 'criclive_stag',
        'ENGINE': 'django.db.backends.mysql',
 
        #prod
        'USER': 'root',
#        'PASSWORD': 'xatr0a',
        'HOST': '127.0.0.1',
#         #local
#         'USER': 'root',
         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
 
        'PORT': '3306',
        'DEFAULT-CHARACTER-SET' : 'utf8',
        'ATOMIC_REQUESTS': True,
        
        'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },
    }

}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# un-comment STATIC_ROOT and comment STATICFILES_DIRS for prod
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)


# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )
# 
# ALLOWED_HOSTS = [
#     'cric.sa.zain.com',  # Allow domain and subdomains
#     'cricboom.com',  # Also allow FQDN and subdomains
#     'cric-live.net',
#     '54.186.108.93',
#     '54.149.245.213',
# ]
#  
#  
# LOGIN_URL = 'criclive_login'
# LOGOUT_URL = 'criclive_logout'
# LOGIN_REDIRECT_URL = 'scoring_matches_list'
#  
# # CELERY SETTINGS
# BROKER_URL = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'



