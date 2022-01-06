# Default settings file for the website
PORT = 80
ENABLE_HTTPS = False
#ENABLE_LOGGING = False

try:
	from settings_local import *
except ImportError:
	raise Exception("Please create settings_local.py")