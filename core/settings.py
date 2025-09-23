import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG') == 'True'
ALLOWED_HOSTS = ['*']


# Application definition
# ----------------------------------------------------------------------------------------------------------------------
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'django_summernote',
    'tailwind',
    'django_browser_reload',
    'ui',

    # Main app
    'register.apps.RegisterConfig',

    'apps.home.apps.HomeConfig',
    'apps.education.apps.EducationConfig',
]


# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'core.middleware.CustomLocaleMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'core.middleware.AllowIframeMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

USE_ACCEPT_LANGUAGE_HEADER = False
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'ui/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.categories',
                'core.context_processors.faculties',
                'core.context_processors.divisions'
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_USER_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
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


# Internationalization
# ----------------------------------------------------------------------------------------------------------------------
LANGUAGES = (
    ('kk', _('Kazakh')),
    ('ru', _('Russian')),
    ('en', _('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'kk'
MODELTRANSLATION_LANGUAGES = ('kk', 'ru', 'en', )
MODELTRANSLATION_TRANSLATION_FILES = (
    'register.translations.publics',
    'register.translations.university',
    'register.translations.content',
)

LOCALE_PATHS = [
    BASE_DIR / 'locales'
]

LANGUAGE_CODE = 'kk'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True


# Templates settings
# ----------------------------------------------------------------------------------------------------------------------
TAILWIND_APP_NAME = 'ui'

# Messages
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

MESSAGE_TAGS = {
    messages.SUCCESS: 'text-green-600',
    messages.WARNING: 'text-amber-600',
    messages.INFO: 'text-blue-600',
    messages.ERROR: 'text-red-600',
}


# Static files (CSS, JavaScript, Images)
# ----------------------------------------------------------------------------------------------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ui/static/')]


# Default primary key field type
# ----------------------------------------------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS, API settings
# ----------------------------------------------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']
