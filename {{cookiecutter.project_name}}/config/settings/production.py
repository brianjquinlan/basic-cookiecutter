from .common import *
# obviously not done

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

