import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%yxc&s2vg&-y)2f@3%ix_m6@3y9vlr10350^gnib4*o=pm2vn&'

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cart',
    'accounts',    
    'django_forms_bootstrap',
    'products',    
    'purchase',    
    'orders',    
    'core',    
    'checkout',        
    'easy_thumbnails',
]

#Setting authorisation to use the defined model, not default
AUTH_USER_MODEL = 'accounts.User'
#To force Django to use the bespoke email/pw authentication, not the default username/pw
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
)


MIDDLEWARE = [
    # Simplified static file serving.
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'shop_proj.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'shop_proj.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# If going to add App specific img/css then use:
# STATICFILES_DIRS = (os.path.join(
#    BASE_DIR, "my_app", "static"),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), ("products", "static"), ("purchase", "static"), ("cart", "static"), ("checkout", "static"), ("orders", "static"), ("core", "static"),)

#Compressing static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'


THUMBNAIL_ALIASES = {
    '': {
            'list-small': {'size': (150, 75), 'crop': 'scale', 'upscale': True,},
            'list-medium': {'size': (300, 150), 'crop': 'scale', 'upscale': True,},
            'list-large': {'size': (400, 200), 'crop': 'scale', 'upscale': True,}
    },
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
 )
