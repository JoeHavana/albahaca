from __future__ import absolute_import, unicode_literals
from .base import *
import os


env = os.environ.copy()
#SECRET_KEY = env['SECRET_KEY']

SECRET_KEY='jqfb(93junty)4_e50gm7&rh$=-0*3q3vv3j!ara6nk7w9@5i8'

ALLOWED_HOSTS = ['127.0.0.1', 'albahaca-example.herokuapp.com']

DEBUG = False


COMPRESS_OFLINE = True
COMPRESS_CSS_FILTERS = [
	'compressor.filters.css_default.CssAbsoluteFilter',
	'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# Once dj-database-url installed
if os.getcwd() == '/app':
	import dj_database_url
	db_from_env = dj_database_url.config(conn_max_age=500)
	DATABASES['default'].update(db_from_env)
	SECURE_PROXY_SSL_HEADER = ('HTTP_X_FOWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
