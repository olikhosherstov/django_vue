"""
WSGI config for vueapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# assuming your django settings file is at '/home/tennisvyshneve/mysite/mysite/settings.py'
# and your manage.py is is at '/home/tennisvyshneve/mysite/manage.py'
path = '/home/tennisvyshneve/django_vue'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'vueapi.settings'

# then:
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())

from whitenoise import WhiteNoise
application = WhiteNoise(application, root='/home/tennisvyshneve/django_vue/static')
