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
        'NAME': os.path.join(BASE_DIR , 'project.db.sqlite3'),
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
    # "django.contrib.humanize", # Handy template tags
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

# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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
# *** Email Configuration ***
# ----------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env.str(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ----------------------------------------------------
# *** Internationalization ***
# ----------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# ----------------------------------------------------
# *** Other Definition ***
# ----------------------------------------------------

SITE_ID = 1
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Session Cookie Age
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month
# Default URL's
HOME_URL = "/"
ADMIN_LOGIN_URL = "/admin/login"
LOGIN_URL = ADMIN_LOGIN_URL

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
# FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
# FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)

# ----------------------------------------------------
# *** Static and Media Files Configuration ***
# ----------------------------------------------------

public_root = root.path('public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

STATIC_ROOT = public_root('static')
STATIC_URL = env.str('STATIC_URL', default='/static/')
STATICFILES_DIRS = [
    os.path.join(public_root, 'staticfiles'),
]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ----------------------------------------------------
# *** SECURITY ***
# ----------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Numan Ibn Mazid""", "numanibnmazid@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# ----------------------------------------------------
# *** --------------- Third Party --------------- ***
# ----------------------------------------------------

# ----------------------------------------------------
# *** Django WhiteNoise ***
# ----------------------------------------------------

# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

if not "whitenoise.middleware.WhiteNoiseMiddleware" in MIDDLEWARE:
    # Must insert after SecurityMiddleware
    MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

# forever-cacheable files and compression support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------------------------------------
# *** Django Compressor ***
# ----------------------------------------------------

# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation

INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]


# ----------------------------------------------------
# *** Django Cors Headers ***
# ----------------------------------------------------

if not "corsheaders" in INSTALLED_APPS:
    INSTALLED_APPS += ["corsheaders"]

if not "corsheaders.middleware.CorsMiddleware" in MIDDLEWARE:
    MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")
