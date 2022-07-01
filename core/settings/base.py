import os
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "yourdomain.com"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "basket",
    "account",
    "phone_field",
    "payment",
    "orders",
    "mptt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

COUNTRIES_FLAG_URL = os.path.join(STATIC_URL, "flags/{code}_16.png")

# Basket session ID
BASKET_SESSION_ID = "basket"

# Custom user model
AUTH_USER_MODEL = "account.UserBase"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

PASSWORD_RESET_TIMEOUT_DAYS = 2

# Email Setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe Payment
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_ENDPOINT_SECRET = env("STRIPE_ENDPOINT_SECRET")
# stripe listen --forward-to localhost:8000/payment/webhook/
