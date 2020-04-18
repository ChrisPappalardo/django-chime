# -*- coding: utf-8 -*-
'''

test_settings
-------------

django test settings
'''

SECRET_KEY = 'test-key'
USE_TZ = True
TIME_ZONE = 'UTC'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_chime.apps.ChimeConfig',
    'tests',
]
