import os
from .base import *  # noqa

# Medhat
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("****++++---- BASE_DIR: " + BASE_DIR)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Medhat

DEBUG = bool(os.environ.get('DJANGO_DEBUG', 'true'))

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
