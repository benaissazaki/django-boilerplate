# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Mailing 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'