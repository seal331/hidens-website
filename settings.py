# Default settings file for the website
PORT = 80
ENABLE_HTTPS = False
ENABLE_LOGGING = False
SERVE_STATIC = False
SERVE_STORAGE = False
TARGET_HOST = 'hiden.ooguy.com'

try:
	from settings_local import *
except ImportError:
	raise Exception("Please create settings_local.py")