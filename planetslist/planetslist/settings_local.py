# coding: utf-8
import os
from settings import *

DATABASES = {
	'default': {
		'ENGINE'  : 'django.db.backends.mysql',
		'NAME'    : 'planets',
		'USER'    : 'root',
		'PASSWORD': '112358',
		'HOST'    : '',
		'PORT'    : '',
	}
}

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'planets',
)

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

# PROJECT_ROOT = '/home/gregory/work/planets-list/planetslist'
# FIXTURE_DIRS = os.path.join(PROJECT_ROOT, 'planets', 'fixtures')