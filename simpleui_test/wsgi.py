"""
WSGI config for simpleui_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('C:/Users/mlzboy/Bitnami Django Stack projects/simpleui_test')
#sys.path.append('C:/Users/mlzboy/Bitnami Django Stack projects/simpleui_test/simpleui_test')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/mlzboy/Bitnami Django Stack projects/simpleui_test/egg_cache")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simpleui_test.settings')

application = get_wsgi_application()
