from .base import*

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
# Build paths inside the project like this: BASE_DIR / 'subdir'.


environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "-5s12kt3piui3lk0iwnm$3!9a^^tp2j#9402kg3ww@9k#g9yh="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
