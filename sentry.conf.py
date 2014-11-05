from os import environ
from urlparse import urlparse

import dj_database_url

# default configuration
from sentry.conf.server import *


DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/direct-sentry')
}

# No trailing slash!
# The sentry service base url http://sentry.example.com
SENTRY_URL_PREFIX = environ.get('SENTRY_URL_PREFIX', '')

# Random secret key
SENTRY_KEY = environ.get('SENTRY_KEY', '')

# Web Service
SENTRY_WEB_HOST = 'localhost'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,
    'limit_request_line': 0,  # required for raven-js
}

# HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Redis backend
REDIS = urlparse.urlparse(environ.get('REDISCLOUD_URL', 'redis://localhost:6379'))
SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': REDIS.hostname,
            'port': REDIS.port,
            'password': REDIS.password,
        }
    }
}

# Mailing
MANDRILL_API_KEY = environ.get('MANDRILL_APIKEY', '')
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
EMAIL_SUBJECT_PREFIX = '[Sentry] '
