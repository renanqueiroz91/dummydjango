SECRET_KEY = 'YOUR SECRET KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'DBUSER',
        'PASSWORD': 'DBPASSWORD',
    }
}
