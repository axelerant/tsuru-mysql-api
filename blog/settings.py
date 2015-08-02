# Copyright 2012 Globo.com. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# Django settings for blog project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE_NAME', 'blog'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'root'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', ''),
    }
}

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '*g$9t&amp;ko6kw-_hkjftrc(&amp;ek68_vm!_yv@#5sv2#03w!4g0d4+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "blog.api.middleware.ExceptionLoggingMiddleware",
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'blog.posts',
    "blog.api",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
RESERVED_NAMES = ("mysql", "test", "information_schema", "mysqlapi")
SHARED_SERVER = os.environ.get("MYSQLAPI_SHARED_SERVER")
SHARED_SERVER_PUBLIC_HOST = os.environ.get(
    "MYSQLAPI_SHARED_SERVER_PUBLIC_HOST",
    SHARED_SERVER,
)
SHARED_USER = os.environ.get("MYSQLAPI_SHARED_USER", "root")
SHARED_PASSWORD = os.environ.get("MYSQLAPI_SHARED_PASSWORD", "")

USE_POOL = os.environ.get("MYSQLAPI_USE_POOL", "False") in \
    ("True", "true", "1")

EC2_ENDPOINT = os.environ.get("MYSQLAPI_EC2_ENDPOINT")
EC2_PORT = os.environ.get("MYSQLAPI_EC2_PORT")
EC2_PATH = os.environ.get("MYSQLAPI_EC2_PATH")
EC2_ACCESS_KEY = os.environ.get("MYSQLAPI_EC2_ACCESS_KEY")
EC2_SECRET_KEY = os.environ.get("MYSQLAPI_EC2_SECRET_KEY")
EC2_AMI = os.environ.get("MYSQLAPI_EC2_AMI")
EC2_KEY_NAME = os.environ.get("MYSQLAPI_EC2_KEY_NAME")
EC2_POLL_INTERVAL = int(os.environ.get("MYSQLAPI_EC2_POLL_INTERVAL", 10))

S3_ACCESS_KEY = os.environ.get("TSURU_S3_ACCESS_KEY_ID")
S3_SECRET_KEY = os.environ.get("TSURU_S3_SECRET_KEY")
S3_BUCKET = os.environ.get("TSURU_S3_BUCKET")

SALT = os.environ.get("MYSQLAPI_SALT", "")

ALLOWED_HOSTS = [
    os.environ.get("MYSQLAPI_ALLOWED_HOST", "localhost"),
]
