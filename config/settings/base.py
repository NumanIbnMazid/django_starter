import os
import environ
from django.core.exceptions import ImproperlyConfigured

def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)

root = environ.Path(__file__) - 3  # get root of the project

# ----------------------------------------------------
# *** Project Environment ***
# ----------------------------------------------------

DEFAULT_ENV_PATH = root
DEFAULT_ENV_FILE = DEFAULT_ENV_PATH.path('.env')()

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env(env.str('ENV_PATH', DEFAULT_ENV_FILE))  # reading .env file

# ----------------------------------------------------
# *** Project's BASE DIRECTORY ***
# ----------------------------------------------------

BASE_DIR = root()

# ----------------------------------------------------
# *** Project's SECRET KEY ***
# ----------------------------------------------------
SECRET_KEY = get_env_value('SECRET_KEY')

# ----------------------------------------------------
# *** Debug Configuration ***
# ----------------------------------------------------

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

# ----------------------------------------------------
# *** Database Configuration ***
# ----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'projectDB',
    }
}

# ----------------------------------------------------
# *** Application Definition ***
# ----------------------------------------------------

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + THIRD_PARTY_APPS + LOCAL_APPS

# ----------------------------------------------------
# *** Middleware Definition ***
# ----------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------
# *** Template Definition ***
# ----------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# ----------------------------------------------------
# *** Authentication Definition ***
# ----------------------------------------------------

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

# ----------------------------------------------------
# *** Internationalization ***
# ----------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------
# *** Other Definition ***
# ----------------------------------------------------

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Session Cookie Age
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month
# Default URL's
HOME_URL = "/"
ADMIN_LOGIN_URL = "/admin/login"
LOGIN_URL = ADMIN_LOGIN_URL

# ----------------------------------------------------
# *** Static and Media Files Configuration ***
# ----------------------------------------------------

public_root = root.path('public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = env.str('MEDIA_URL', default='media/')

STATIC_ROOT = public_root('static')
STATIC_URL = env.str('STATIC_URL', default='static/')
STATICFILES_DIRS = [
    os.path.join(public_root, 'staticfiles'),
]