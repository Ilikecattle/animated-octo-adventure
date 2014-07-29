import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = ')#rns-h9guyb6db=%g5!$4!6_tkzt1f-hyi%-(40lh)z+*)tr^'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'games',
    'common',
    'caroftheday',
    'carquizgame',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'  
LOGIN_URL = '/accounts/signin/'  
LOGOUT_URL = '/accounts/signout/'  

ROOT_URLCONF = 'catharticgames.urls'

WSGI_APPLICATION = 'catharticgames.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.Profile'

MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'

FORCE_SCRIPT_NAME = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'catharticgames.db'),
    }
}

STATICFILES_DIRS = (
    BASE_DIR + '/catharticgames/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = BASE_DIR + '/static/'
STATIC_URL = '/static/'
