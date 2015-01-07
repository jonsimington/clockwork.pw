import os

SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)

##################################################################
#
# SECRET SETTINGS
#
##################################################################
try:
    from secret_settings import *
except ImportError:
    print "Couldn't find secret_settings file. Creating a new one."
    secret_settings_loc = os.path.join(SETTINGS_DIR, "secret_settings.py")
    with open(secret_settings_loc, 'w') as secret_settings:
        secret_key = ''.join([chr(ord(x) % 90 + 33) for x in os.urandom(40)])
        secret_settings.write("SECRET_KEY = '''%s'''\n" % secret_key)
    from secret_settings import *    


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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    # for django-admin-tools
    'django.core.context_processors.request',

    # django allauth
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',

    # blog
    'zinnia.context_processors.version',

    # forums
    'pybb.context_processors.processor',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

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
    'django.contrib.sites',

    # django crispy forms
    'crispy_forms',    

    # site apps
    'clockwork',
    'clockwork.home',
    'clockwork.profiles',
    'clockwork.utility',
    
    # Django Allauth
    'allauth',
    'allauth.account',

    # Blog
    'zinnia',
    'tagging',
    'mptt',
    'django_comments',

    # forums
    'pybb',
    'bootstrapform',
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

    #forums
    'pybb.middleware.PybbMiddleware',
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

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = True

USE_TZ = True

###################################################################
#
# STATIC SETTINGS
#
###################################################################
STATIC_URL = '/static/'
STATIC_ROOT = '/home/jonsimington/clockwork.pw/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

###################################################################
#
# BLEACH SETTINGS
#
##################################################################
import bleach

ALLOWED_HTML_TAGS = bleach.ALLOWED_TAGS + ['h1', 'h2', 'h3', 'p', 'img']

ALLOWED_HTML_ATTRS = bleach.ALLOWED_ATTRIBUTES
ALLOWED_HTML_ATTRS.update({'img': ['src', 'alt'],})

##################################################################
#
# AUTHENTICATION SETTINGS
#
##################################################################

# Redirect to / upon login
LOGIN_REDIRECT_URL = "/"

# Users don't have to provide an email address when registering
ACCOUNT_EMAIL_REQUIRED = False

# Users don't need to verify their email address since it's not required
ACCOUNT_EMAIL_VERIFICATION = False

# Email settings
ACCOUNT_EMAIL_SUBJECT_PREFIX = "<Clockwork>"

ACCOUNT_AUTHENTICATION_METHOD = "username"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PROFILE_MODEL = 'profiles.models.UserProfile'

ANONYMOUS_USER_ID = -1

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/profile/%s/" % u.username,
}

SITE_ID = 1

###################################################################
#
# FORUM SETTINGS
#
###################################################################
PYBB_PROFILE_RELATED_NAME = 'profile'
PYBB_DEFAULT_AVATAR_URL = 'http://i.imgur.com/ytOAIRY.png'
PYBB_DEFAULT_TITLE = "<Clockwork> Forums"
PYBB_MARKUP = 'bbcode'
PYBB_MARKUP_ENGINE_PATHS = {
    'bbcode': 'pybb.markup.bbcode.BBCodeParser',
    'markdown': 'pybb.markup.markdown.MarkdownParser',
}
AVATAR_DIR = '/home/jonsimington/clockwork.pw/pybb/avatar/'


###################################################################
#
# PRODUCTION SETTINGS
#
###################################################################
USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'clockwork.pw',
    '.clockwork.pw',
]
