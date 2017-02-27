#CORE SETTINGS

ABSOLUTE_URL_OVERRIDES = {}

#who get code error notifications
ADMINS =  [('NAvas', 'navasmc1@gmail.com'), ('test', 'navasmc@yahoo.com')] 
#host/domain names that this Django site can serve
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

#Default: True
#When set to True, if the request URL does not match any of the patterns in the URLconf and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a slash appended
APPEND_SLASH = True

#Need*
#You can cache any Python object that can be pickled safely: strings, dictionaries, lists of model objects, and so forth.
#BACKEND,KEY_FUNCTION,KEY_PREFIX,LOCATION,OPTIONS,TIMEOUT,VERSION,CACHE_MIDDLEWARE_ALIAS....
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache','django.core.cache.backends.db.DatabaseCache'
    }
}

#Databases
#CHARSET¶,COLLATION,DEPENDENCIES,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',#mysql,sqlite3,oracle,postgresql
        'NAME': 'mydatabase',
        'TIME_ZONE':'Asia/Dubai',#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        'TEST': {
            'NAME': 'mytestdatabase',
        },
     },
    #'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'mydatabase',
    #     'USER': 'mydatabaseuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
}
#Default:2621440 (i.e. 2.5 MB)
#The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440 
#Default: 1000
#The maximum number of parameters that may be received via GET or POST before a SuspiciousOperation (TooManyFields) is raised
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
#The list of routers that will be used to determine which database to use when performing a database query
#Default: []
DATABASE_ROUTERS = []
#The default formatting to use for displaying date fields in any part of the system
#Default: 'N j, Y' (e.g. Feb. 4, 2003)
DATE_FORMAT = 'N j, Y'
#A list of formats that will be accepted when inputting data on a date field
# DATE_INPUT_FORMATS = [
#     '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
#     '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
#     '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
#     '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
#     '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
# ]
#Default: 'N j, Y, P' (e.g. Feb. 4, 2003, 4 p.m.)
#DATETIME_FORMAT = 'N j, Y, P'
#DATETIME_INPUT_FORMATS = [
#     '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
#     '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
#     '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
#     '%Y-%m-%d',              # '2006-10-25'
#     '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
#     '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
#     '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
#     '%m/%d/%Y',              # '10/25/2006'
#     '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
#     '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
#     '%m/%d/%y %H:%M',        # '10/25/06 14:30'
#     '%m/%d/%y',              # '10/25/06'
# ]
DEBUG = True
DECIMAL_SEPARATOR = '.'
#Default charset to use for all HttpResponse objects, if a MIME type isn’t manually specified
DEFAULT_CHARSET = 'utf-8'
#Default: 'text/html'
#Default content type to use for all HttpResponse objects, if a MIME type isn’t manually specified
DEFAULT_CONTENT_TYPE = 'text/html'
##..
##..
#Default: 'webmaster@localhost'
#'webmaster@localhost'
DEFAULT_FROM_EMAIL = 'no-reply@navas.com'
#Default tablespace to use for indexes on fields that don’t specify one, if the backend supports it
#Default: '' (Empty string)
DEFAULT_INDEX_TABLESPACE = ''
#Default tablespace to use for models that don’t specify one, if the backend supports it
DEFAULT_TABLESPACE = ''

#List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide
#DISALLOWED_USER_AGENTS = []
#Default: 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND=''
#The directory used by the file email backend to store output file
#EMAIL_FILE_PATH=Not defind
#Default: 'localhost'
#The host to use for sending email.
#EMAIL_HOST='localhost'
#Email host user
#Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won’t attempt authentication
#EMAIL_HOST_USER = ''
#EMAIL_PORT = 25
#EMAIL_SUBJECT_PREFIX = ''
#EMAIL_USE_TLS = false
##..
##..
#Language
# full Python path to a Python package that contains format definitions for project locales.If not None, Django will check for a formats.py file, under the directory named as the current locale, and will use the formats defined in this file
# FORMAT_MODULE_PATH = [
#     'mysite.formats',
#     'some_app.formats',
# ]

INSTALLED_APPS = [    
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user'
    ]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_COOKIE_AGE = None
LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]
#Translation file
LOCALE_PATHS = [
    '/home/www/project/common_files/locale',
    '/var/local/translations/locale',
]
#LOGGING = 'django/utils/log.py'
#A list in the same format as ADMINS that specifies who should get broken link notifications when BrokenLinkEmailsMiddleware is enabled
MANAGERS = ['navasmc1@gmail.com']
#Absolute filesystem path to the directory that will hold user-uploaded files.
# "/var/www/example.com/media/"
MEDIA_ROOT = '/var/www/example.com/media/'
MEDIA_URL = '/media/'
#Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or outpu
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# The root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME