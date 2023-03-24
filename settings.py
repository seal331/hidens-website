# Default settings file for the website
PORT = 80
ENABLE_LOGGING = False
LOG_TO_FILE = False
TESTING = False
SERVE_STATIC = False
SERVE_STORAGE = False
SERVE_JS = False
ROLLOUT_MODE = False
MCHOST = 'hiden.pw'
MCPORT = 25565
APRILFOOLS_2022 = False
APRILFOOLS_2023 = False

# Import settings from settings_local.py. If settings_local.py is not present, terminate
try:
	from settings_local import *
except ImportError:
	raise Exception("settings_local.py not found, please create it.")