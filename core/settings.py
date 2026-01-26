import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG') == 'True'
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')


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
    'ckeditor',
    'tailwind',
    'ui',
    'register.apps.RegisterConfig',

    'apps.home.apps.HomeConfig',
    'apps.education.apps.EducationConfig',
]


# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'core.middleware.ForceKazakhLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'core.middleware.AllowIframeMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

if DEBUG:
    INSTALLED_APPS += ['django_browser_reload']
    MIDDLEWARE += [
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
                'core.context_processors.global_context',
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

LANGUAGE_COOKIE_NAME = 'language'

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


# CKEditor settings
# ----------------------------------------------------------------------------------------------------------------------
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'defaultLanguage': 'ru',
        'width': 840,
        'height': 420,
        'removePlugins': 'autogrow',

        'toolbar': [
            {
                'name': 'styles',
                'items': ['Format']
            },
            {
                'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList', 'BulletedList', '-',
                    'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                ]
            },
            {
                'name': 'insert',
                'items': ['Image', 'Table', 'Mathjax', ]
            },
            {
                'name': 'document',
                'items': ['Source', '-', 'Preview', '-', 'Maximize']
            },
        ],
        'format_tags': 'p;h2;h3;h4',

        'mathJaxLib': 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,

        'extraPlugins': ','.join([
            'mathjax',
            'uploadimage',
            'autogrow',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    }
}