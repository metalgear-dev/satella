"""
Django settings for indexsite project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6$zvpxoksvm2ennzzt@ofp3t-k+=)t3bap$t5oh(t9n+a_*bi#'

# SECURITY WARNING: don't run with debug turned on in production!
# デバッグ機能
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'contract_index.apps.ContractIndexConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'indexsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'indexsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    
        'NAME': 'db_satella',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# ログイン後トップページにリダイレクト
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# セッションクッキーの寿命:8時間
SESSION_COOKIE_AGE = 8 * 3600
# 毎リクエストでセッション更新(アクティブならセッション切れしない)
SESSION_SAVE_EVERY_REQUEST = True

# Fetch Django's project directory
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Fetch the project_root
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MIDDLEWARE_CLASSES = (
    # 一番最後に以下の3行を追記する
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

# さらに、 CACHES も追記
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'sample_cache',
        'TIMEOUT': 60 * 10,
        'OPTIONS': {
            'MAX_ENTRIES': 10000, 
            'CULL_FREQUENCY': 2,
        },
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 10 # 10 分（デフォルト）

# ログ用設定-----------------------------------------------
LOGGING = {
    'version': 1,
    'formatters': {
        'all': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "message:%(message)s",
                "process:%(process)d",
                "thread:%(thread)d",
            ])
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'formatter': 'all',  # どの出力フォーマットで出すかを名前で指定
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'all'
        },
    },
    'loggers': {
        'command': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
}

# 本番環境用の書き換え---------------------------------------

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'contract_index',
#         'USER': 'root',
#         'PASSWORD': 'we+G7?ujBI',
#         'HOST': '',
#         'PORT': '3306',
#     }
# }
# DEBUG = False

# デバッグツール用------------------------------------------
if DEBUG:
    # 本番環境でのデバッグはここのIPアドレスを変更
    INTERNAL_IPS = ('127.0.0.1', '172.25.40.219')
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    # 表示する内容
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

DATA_UPLOAD_MAX_MEMORY_SIZE = 100000000