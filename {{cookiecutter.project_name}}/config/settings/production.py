from .common import *

# Secret key
SECRET_KEY = env('DJANGO_SECRET_KEY')

# domain names valid for site
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# Email Setting with anymail and mailgun
INSTALLED_APPS += ['anymail']

ANYMAIL = {
        'MAILGUN_API_KEY' : env('DJANGO_MAILGUN_KEY')
        'MAILGUN_SENDER_DOMAIN' : env('DJANGO_DOMAIN')

}

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL')
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX')

# sessions in cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

{% if cookiecutter.redis == 'yes' %}

# caching with redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'{env("REDIS_URL", default="redis://127.0.0.1:6379")}/{0}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

{% else %}

# caching with memcache
INSTALLED_APPS += ['memcache_status']

# need to add to specific spots
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware', # memcache
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', # memcache
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211'
        }
}

{% endif %}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15 # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = '{{ cookiecutter.project_name }}' 

# database config
DATABASES['default'] = env.db('DATABASE_URL')

# template config
# add cache loader to templates
TEMPLATES[0]['OPTIONS']['loaders'] = [('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader',
    ]),
]

# security settings
# security settings
SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False # want to read the cookie for ajax post
X_FRAME_OPTIONS = 'DENY'

INSTALLED_APPS += ['gunicorn']


# static settings using whitenoise
STATIC_ROOT = str(APPS_DIRS.path('staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE_CLASSES = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE_CLASSES

# media settings
INSTALLED_APPS += ['storages']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET')
AWS_S3_FILE_OVERWRITE = False

MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# logging 
INSTALLED_APPS += ['raven.contrib.django.raven_compat']
# MIDDLEWARE_CLASSES = ['raven.contrib.django.raven_compat.middleware.SentryReponseErrorIdMiddleware'] + MIDDLEWARE_CLASSES

RAVEN_CONFIG = {
    'dsn' : env('SENTRY_DSN')
}

SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
