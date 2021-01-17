"""
WSGI config for pysonet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
# add the hellodjango project path into the sys.path
sys.path.append('<PATH_TO_MY_DJANGO_PROJECT>/config')

# add the virtualenv site-packages path to the sys.path
sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
