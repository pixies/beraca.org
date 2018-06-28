import os
import environ
import datetime

# Localizate the root dir, two levels above
ROOT_DIR = environ.Path(__file__) - 2
APPS_DIR = ROOT_DIR.path('ibcommunity')

# Loads .env file
env = environ.Env()
env.read_env(os.path.join(ROOT_DIR(), '.env'))



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('IB_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #env.bool('IB_DEBUG')

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env.list('IB_ALLOWED_HOSTS')


# Application definition


DEFAULT_APPS = [
    # 'grappelli',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'djoser',
    'material',
    'corsheaders'
]

LOCAL_APPS = [
    'accounts.apps.AccountsConfig',
    'address',
    'community',
    'company',
    'product',
    'project',
    'providers',
    'family',
    'client',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ibcommunity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'ibcommunity.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': env.db('IB_DATABASE_URL', default='postgres:///ib')
}

# LOGGING
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'mail_admins'],
                'propagate': True
            }
        }
    }

# New User Base
AUTH_USER_MODEL = 'accounts.MyUser'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Settings

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


LOGIN_REDIRECT_URL = '/index/search/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Rest Framework Setup

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),

    'JWT_PAYLOAD_HANDLER':
    #'rest_framework_jwt.utils.jwt_payload_handler',
    'accounts.api.jwtutils.jwt_payload_handler',

    #'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    #'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'accounts.api.jwtutils.jwt_response_payload_handler',

}

# Cors Configuration
CORS_ORIGIN_ALLOW_ALL = True

# Celery
CELERY_BROKER_URL = 'amqp://localhost'

# Email configuration
"""
DEFAULT_FROM_EMAIL = env('IB_EMAIL_ADDR')
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SENDGRID_API_KEY = "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"
SENDGRID_SANDBOX_MODE_IN_DEBUG = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = '3ecologias'
EMAIL_HOST_PASSWORD = 'Tatub0lana0b0la'
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
"""
