from .base import *

# ----------------------------------------------------
# *** Allowed Hosts ***
# ----------------------------------------------------

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")

# ----------------------------------------------------
# *** Databases ***
# ----------------------------------------------------

DATABASES = {'default': env.db('DATABASE_URL')}

# ----------------------------------------------------
# *** Debug ***
# ----------------------------------------------------

DEBUG = False

# ----------------------------------------------------
# *** Templates ***
# ----------------------------------------------------

TEMPLATES[0]["DIRS"] = [os.path.join(root.path(), "templates")]

# ----------------------------------------------------
# *** Whitenoise ***
# ----------------------------------------------------

# INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# # Must insert after SecurityMiddleware, which is first in settings/common.py
# if not "whitenoise.middleware.WhiteNoiseMiddleware" in MIDDLEWARE:
#     MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")