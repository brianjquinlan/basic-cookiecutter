"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    from raven.contrib.django.raven_compat.middleware.wsge import Sentry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_name}}.settings")

application = get_wsgi_application()
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.setings.production':
    application = Sentry(application)
