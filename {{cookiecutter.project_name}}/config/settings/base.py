"""
Django settings for {{cookiecutter.project_name}} project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import environ
env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('{{cookiecutter.project_name}}')

# Debug
DEBUG = env.bool('DJANGO_KEY', False)

#ALLOWED_HOSTS = []


# Application config
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
    # apps you create go here
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS 

# middleware config
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# if you want to use sqlite 
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(str(ROOT_DIR), 'db.sqlite3'),
#    }
# }

DATABASES = {
        'default': env.db('DATABASE_URL'), # example 'postgres:///db_name'
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# templates config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
			str(APPS_DIR.path('templates'))
		],
        'OPTIONS': {
			'debug': DEBUG,
			'loaders' : [
				'django.template.loaders.filesystem.Loader',	
				'django.template.loaders.app_directories.Loader',
			],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# what's used to send emails
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')

# admins of site
ADMINS = (
	("""{{cookiecutter.author}}""", '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(APPS_DIR.path('static')
]

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = str(APPS_DIR('media'))

# url config
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


ADMIN_URL = r'^admin/'
