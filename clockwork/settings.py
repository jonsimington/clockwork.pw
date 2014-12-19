import os

from secret_settings import SECRET_KEY

SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

####################################################################
#
# TEMPLATE SETTINGS
#
###################################################################

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

ALLOWED_HOSTS = []

####################################################################
#
# INSTALLED APPS
#
####################################################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'clockwork',
    'clockwork.home',
)

###################################################################
#
# MIDDLEWARES
#
###################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

###################################################################
#
# URL SETTINGS
#
###################################################################
ROOT_URLCONF = 'clockwork.urls'


WSGI_APPLICATION = 'clockwork.wsgi.application'


###################################################################
#
# DATABASE SETTINGS
#
###################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

###################################################################
#
# TIMEZONE SETTINGS
#
###################################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

###################################################################
#
# STATIC SETTINGS
#
###################################################################

STATIC_URL = '/static/'
