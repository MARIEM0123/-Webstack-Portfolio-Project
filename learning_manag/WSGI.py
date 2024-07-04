"""
WSGI config
WEB SERVER GATEWAY INTERFACE
TO RUN PYTHON APPLICATION
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')

application = get_wsgi_application()
