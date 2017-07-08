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

# sessions in cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

{% if cookiecutter.redis == 'yes' %}

# caching with redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
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
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# static settings using whitenoise
STATIC_ROOT = str(APPS_DIRS.path('staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# media settings

# logging 
