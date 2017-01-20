#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Production settings
- Run in production mode
- Use Amazon's S3 for storing static files
"""

from .base import *

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = [".alegpaez.com"]

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

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = str(PROJECT_DIR('staticfiles'))

MEDIA_URL = '/media/'
MEDIA_ROOT = str(PROJECT_DIR('media'))