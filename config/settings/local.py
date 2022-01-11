from .base import *

# ----------------------------------------------------
# *** Allowed Hosts ***
# ----------------------------------------------------

ALLOWED_HOSTS = ['*']

# ----------------------------------------------------
# *** Databases ***
# ----------------------------------------------------

if os.environ.get('DATABASE_URL') is not None:
    DATABASES = {'default': env.db('DATABASE_URL')}

# remove sslmode for local development
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)
# set atomic requests
# DATABASES["default"]["ATOMIC_REQUESTS"] = True

# ----------------------------------------------------
# *** Debug ***
# ----------------------------------------------------

DEBUG = True

# ----------------------------------------------------
# *** Templates ***
# ----------------------------------------------------

TEMPLATES[0]["DIRS"] = [os.path.join(root.path(), "templates")]

# ----------------------------------------------------
# *** --------------- Third Party --------------- ***
# ----------------------------------------------------

# ----------------------------------------------------
# *** Django WhiteNoise ***
# ----------------------------------------------------

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

if not "whitenoise.middleware.WhiteNoiseMiddleware" in MIDDLEWARE:
    # Must insert after SecurityMiddleware
    MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

# forever-cacheable files and compression support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------------------------------------
# *** Django Debug Toolbar ***
# ----------------------------------------------------

if not "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.append("debug_toolbar")

if not "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = [
    "127.0.0.1", "0.0.0.0", "10.0.2.2"
]

if DEBUG:
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + INTERNAL_IPS


# ----------------------------------------------------
# *** LOGGING ***
# ----------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for more details on how to customize logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}
