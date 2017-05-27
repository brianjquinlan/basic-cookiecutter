from .base import * # noqa?

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGE')

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', True)

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# email console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# caching 
CACHES = {
    'default': {
        'BACKEND':
            'django.core.cache.backends.locmem.LocMemCache',
            # maybe use 'django.core.cache.backends.dummy.DummyCache'
        'LOCATION': 'unique'
    }
}


# django-debug-toolbar
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

# INTERNAL_IPS ? 

# django-extensions?
