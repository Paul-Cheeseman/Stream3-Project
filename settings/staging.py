from .base import *

#To import secret keys not held on GitHub
from .private import *
from django.conf import settings
import stripe


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%yxc&s2vg&-y)2f@3%ix_m6@3y9vlr10350^gnib4*o=pm2vn&'
#A test customer stripe token (allows repeated test use, rather than a one off paymen token) 
STRIPE_TEST_TOKEN = 'cus_C5Y4XV57a4s0xz'


#Stripe Environment Variables:
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_zkkJLlqQ1Tc9XhPXQhJi7QZC')
#STRIPE_SECRET is in private.py, which is ignroed by GIT, to prevent it being uploaded to GitHub
stripe.api_key = settings.STRIPE_SECRET

SITE_URL = 'https://stream-3-project.herokuapp.com'
ALLOWED_HOSTS.append('stream-3-project.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}