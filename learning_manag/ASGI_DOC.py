"""
ASGI config for elearning project.
provide a standard interface between servers, frameworks and applications

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')

application = get_asgi_application()
