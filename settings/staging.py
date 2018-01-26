from .base import *
import dj_database_url

#To import secret keys not held on GitHub
from .private import *
from django.conf import settings
import stripe


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
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

#Compressing static files
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


AWS_STORAGE_BUCKET_NAME = 'stream3img'
AWS_S3_REGION_NAME = 'eu-west-2'  # e.g. us-east-2

#### These are set on heroku as config variables to avoid prying eyes!
#AWS_ACCESS_KEY_ID = 'secret squirrel'
#AWS_SECRET_ACCESS_KEY = 'secret squirrel'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = 's3.%s.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#https://s3.stream3img.amazonaws.com/
#https://eu-west-2.s3.stream3img.amazonaws.com/

#https://s3.eu-west-2.amazonaws.com/stream3img/Yellow_Trousers_2.jpg
#MEDIA_ROOT = "https://%s.%s/" % (AWS_S3_REGION_NAME, AWS_S3_CUSTOM_DOMAIN)
#MEDIA_ROOT = "https://%s.%s/" % (AWS_S3_REGION_NAME, AWS_S3_CUSTOM_DOMAIN)
MEDIA_URL = 'media/'
#THUMBNAIL_MEDIA_ROOT = 'https://s3.eu-west-2.amazonaws.com/stream3img/media/'
#THUMBNAILMEDIA_URL = 'media/'

print("media ROOT")
print(MEDIA_ROOT)


#Point media files to Amazon storage files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'





