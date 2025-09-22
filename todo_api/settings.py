# Add at the top after imports
from pathlib import Path
import os
from corsheaders.defaults import default_headers  # <-- important

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick settings
SECRET_KEY = 'django-insecure-67elygua12g1m+d&c@$o#0e*uz+kb%5q#&pq+@gmcs^bk%d%v@'
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',  # <-- corsheaders app
    'todo',
]

# MIDDLEWARE - CORS must be at the top
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # <-- move this to top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo_api.urls'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",  # your React dev server
]
CORS_ALLOW_HEADERS = list(default_headers) + [
    "content-type",  # allow content-type header
]
CORS_ALLOW_CREDENTIALS = True  # if sending cookies/auth headers

# Templates, WSGI, Database remain the same
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todo_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
