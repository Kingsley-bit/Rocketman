import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False
SECRET_KEY = '8b8l&x-m-@oudvit9))9#o=yu=c3ar^ps59^0me79i@xxvu4+&'  # @todo get a key from here https://miniwebtool.com/django-secret-key-generator/
ALLOWED_HOSTS = ['localhost', 'rocketman.project.com', '+']  # @todo add your website url in here
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx5',
        "HOST": 'localhost',
        "PORT": "",
    }
}


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://0124f8117e75467099dbeea9b259a804@o1287704.ingest.sentry.io/6503227",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass