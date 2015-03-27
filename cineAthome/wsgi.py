"""
WSGI config for cineAthome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cineAthome.settings")

import sys
encoding='utf-8'
reload(sys)
sys.setdefaultencoding(encoding)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
