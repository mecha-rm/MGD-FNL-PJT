"""
Django settings for GEN project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from decouple import config, Csv
import dj_database_url
from django.contrib.messages import constants as messages
from django.utils.log import DEFAULT_LOGGING as LOGGING
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

INTERNAL_IPS = config("INTERNAL_IPS")

# Email settings for sending error notifications to admins and emails
# to users (e.g., password resets)
ADMINS = [
    ("Admin", "admin@maxsimgen.com"),
]
if not DEBUG:
    LOGGING["handlers"]["mail_admins"]["include_html"] = True
    SERVER_EMAIL = config("SERVER_EMAIL")
    DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

### Application definition

INSTALLED_APPS = [
    "admin_interface",
    "modeltranslation",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "widget_tweaks",
    "embed_video",
    "vote",
    "debug_toolbar",
    "social_django",
    "crispy_forms",
    "adminsortable2",
    "django_extensions",
    "import_export",
    "sri",
    "rosetta",
    "maintenance_mode",
    "core",
    "accounts",
    "courses",
    "discussions",
    "dashboard",
    "quiz",
    "videos",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
]

# Provide a lists of languages which your site supports.
LANGUAGES = (
    ("en", _("English")),
    ("fr", _("French")),
)

ROOT_URLCONF = "GEN.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "maintenance_mode.context_processors.maintenance_mode",
            ],
        },
    },
]

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.google.GoogleOpenId",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

WSGI_APPLICATION = "GEN.wsgi.application"

X_FRAME_OPTIONS = "SAMEORIGIN"

### Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}

### Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


### Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
#
# ISO Language Code Table
# http://www.lingoes.net/en/translator/langcode.htm

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

### Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

if not DEBUG:
    STATIC_ROOT = "/home/gen/GEN_static/"
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = "/media/"
if not DEBUG:
    MEDIA_ROOT = "/home/gen/GEN_media/"
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

### Login settings

LOGIN_URL = "login"
LOGOUT_URL = "logout"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

if not DEBUG:
    # Security / HTTPS / TLS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_DOMAIN = "maxsimgen.com"
    CSRF_TRUSTED_ORIGINS = ["maxsimgen.com", "www.maxsimgen.com"]
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SECURE_SSL_REDIRECT = False  # Set to true if nginx is not already redirecting
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_REFERRER_POLICY = "same-origin"
    os.environ["wsgi.url_scheme"] = "https"

### E-mail backend
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = config("SENDGRID_API_KEY")
SENDGRID_TRACK_EMAIL_OPENS = True
SENDGRID_TRACK_CLICKS_HTML = False
SENDGRID_TRACK_CLICKS_PLAIN = False
# Toggle sandbox mode (when running in DEBUG mode)
SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG
# echo to stdout or any other file-like object that is passed
# to the backend via the stream kwarg.
SENDGRID_ECHO_TO_STDOUT = DEBUG


### Maintenance mode settings
# complete list available at
# https://github.com/fabiocaccamo/django-maintenance-mode#configuration-optional

# if True the maintenance-mode will be activated
MAINTENANCE_MODE = None

# if True admin site will not be affected by the maintenance-mode page
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True

# if True the staff will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_STAFF = False

# if True the superuser will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_SUPERUSER = False

# if True the maintenance mode will not return 503 response while running tests
# useful for running tests while maintenance mode is on, before opening the site to public use
MAINTENANCE_MODE_IGNORE_TESTS = False

### Social authentication settings
# Documentation:
# https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html
# https://python-social-auth.readthedocs.io/en/latest/pipeline.html

SOCIAL_AUTH_LOGIN_ERROR_URL = "/settings/"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "home"
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ["username", "first_name", "email"]

SOCIAL_AUTH_GITHUB_KEY = config("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = config("SOCIAL_AUTH_GITHUB_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    "social_core.pipeline.social_auth.social_details",
    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    "social_core.pipeline.social_auth.social_uid",
    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    "social_core.pipeline.social_auth.auth_allowed",
    # Checks if the current social-account is already associated in the site.
    "social_core.pipeline.social_auth.social_user",
    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    "social_core.pipeline.user.get_username",
    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',
    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    "social_core.pipeline.social_auth.associate_by_email",
    # Create a user account if we haven't found one yet.
    "social_core.pipeline.user.create_user",
    # Create the record that associates the social account with the user.
    "social_core.pipeline.social_auth.associate_user",
    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    "social_core.pipeline.social_auth.load_extra_data",
    # Update the user record with any changed info from the auth service.
    "social_core.pipeline.user.user_details",
)
