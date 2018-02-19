from .base import *

#To import secret keys not held on GitHub
from .private import *
from django.conf import settings
import stripe


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition, add to it
INSTALLED_APPS.append('debug_toolbar')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#Stripe Environment Variables:
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_zkkJLlqQ1Tc9XhPXQhJi7QZC')
#STRIPE_SECRET is in private.py, which is ignroed by GIT, to prevent it being uploaded to GitHub
stripe.api_key = settings.STRIPE_SECRET


MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'