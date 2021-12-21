"""
WSGI config for PONTOS_TURISTICOS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

from dj_static import Cling


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PONTOS_TURISTICOS.settings')
application = Cling(get_wsgi_application())

