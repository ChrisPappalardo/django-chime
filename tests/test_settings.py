# -*- coding: utf-8 -*-
'''

test_settings
-------------

django test settings
'''

SECRET_KEY = 'test-key'
USE_TZ = True
TIME_ZONE = 'UTC'

ADMINS = [('test', 'test@example.com')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': 'django_chime',
        'NAME': 'django_chime',
        'TEST': {
            'NAME': 'test',
        },
    },
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_chime.apps.ChimeConfig',
    'crispy_forms',
    'djcorecap',
    'tests',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_chime.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
