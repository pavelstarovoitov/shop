DEBUG = False
ALLOWED_HOSTS = ['*']



DATABASES={
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'db11',
        'USER':'django_shop1',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':'',
    }
}