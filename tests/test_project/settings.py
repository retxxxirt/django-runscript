SECRET_KEY = 'wY2j(CXnx3l(%/vDwjjOS^2d@SaV>[X0>^pr75,Z\JApXnP%Lb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = [
    'django_runscript',
    'test_app'
]
