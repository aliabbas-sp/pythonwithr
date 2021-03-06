from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import utils.exceptionhandler

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'PYTHONWITHRHEROKUDOCKER'
DEBUG = 'True'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'pythonwithr.herokuapp.com', '*']
CSRF_TRUSTED_ORIGINS = ['https://pythonwithr.herokuapp.com', 'https://*', 'http://*']

# Application definition

INSTALLED_APPS = [
    'runr.apps.RunrConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'pythonwithr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'pythonwithr.wsgi.application'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exceptionhandler.custom_exception_handler'
}

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static/',
    BASE_DIR / 'templates/',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "d6n2l3s6b3mh4c",
        "USER": "bevkoljybiazss",
        "PASSWORD": "0e51884d6e41a9489f597b01660edbedc3c37f8ddbf0c73cabf5d61fff1a3514",
        "HOST": "ec2-34-205-46-149.compute-1.amazonaws.com",
        "PORT": 5432,
    }
}
