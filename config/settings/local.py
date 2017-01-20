#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Local settings
- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .base import *  # noqa

import os

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# -----------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# CACHING
# -----------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'NAME': env("DB_DEFAULT_NAME"),
        'ENGINE': env("DB_DEFAULT_ENGINE"),
        'USER': env("DB_DEFAULT_USER"),
        'PASSWORD': env("DB_DEFAULT_PASSWORD"),
        'HOST': env("DB_DEFAULT_HOST"),
        'PORT': env("DB_DEFAULT_PORT"),
    },
    'wordpress': {
        'NAME': env("DB_WORDPRESS_NAME"),
        'ENGINE': env("DB_WORDPRESS_ENGINE"),
        'USER': env("DB_WORDPRESS_USER"),
        'PASSWORD': env("DB_WORDPRESS_PASSWORD"),
        'HOST': env("DB_WORDPRESS_HOST"),
        'PORT': env("DB_WORDPRESS_PORT"),
    }
}

# django-debug-toolbar
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# -----------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# TESTING
# -----------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
STATIC_URL = '/static/'

# MEDIA CONFIGURATION
# -----------------------------------------------------------------------------
MEDIA_ROOT = str(PROJECT_DIR('media'))

MEDIA_URL = '/media/'
