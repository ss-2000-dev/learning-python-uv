import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

STATIC_URL = '/static/'
ROOT_URLCONF = "config.urls"
DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("DJANGO_SECRET_KEY environment variable is not set.")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
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

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "todo" / "templates"
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'mydjangoapp'),
        'USER': os.environ.get('MYSQL_USER', 'mydjangoappuser'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'your_super_strong_app_password'),
        'HOST': os.environ.get('MYSQL_HOST', 'db'), 
        'PORT': int(os.environ.get('MYSQL_PORT', '3306')),
        'OPTIONS': {
            'charset': 'utf8mb4', 
        },
    }
}