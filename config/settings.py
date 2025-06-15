import os
from dotenv import load_dotenv
load_dotenv()

ROOT_URLCONF = "config.urls"
DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("DJANGO_SECRET_KEY environment variable is not set.")