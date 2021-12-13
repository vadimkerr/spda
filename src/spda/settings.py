"""
Django settings for spda project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONTENT_DIR = os.path.join(BASE_DIR, "content")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#uxg=&xmr=gc0)7(m4oz#q1i4sicdn+1*wz%5p_datf5i^^psi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = ["*"]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap4",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "spda.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(CONTENT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "spda.wsgi.application"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = ""
EMAIL_HOST_USER = ""
DEFAULT_FROM_EMAIL = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

ENABLE_USER_ACTIVATION = False
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = "index"
LOGIN_URL = "accounts:log_in"
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
EMAIL_ACTIVATION_AFTER_CHANGING = True

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "en"
LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
]

TIME_ZONE = "UTC"
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(CONTENT_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, "assets"),
]

LOCALE_PATHS = [os.path.join(CONTENT_DIR, "locale")]

SIGN_UP_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "password1",
    "password2",
]
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ["first_name", "last_name", "email", "password1", "password2"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
