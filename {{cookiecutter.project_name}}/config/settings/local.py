
from .base import * # noqa?

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eti-fvopyn=q@rl0z^^$qgbmzc&dtj6p7ej$+$llq7^z^pj*8h'
# change key

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', True)

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# email console backend

# caching 

# django-debug-toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

# INTERNAL_IPS ? 

# django-extensions?
