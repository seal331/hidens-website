# Default settings file for the website
PORT = 80
ENABLE_LOGGING = False
LOG_TO_FILE = False
DEV_MODE = False
SERVE_STATIC = False
SERVE_STORAGE = False
SERVE_JS = False
MCHOST = 'hiden.pw'
MCPORT = 25565
GMODHOST = 'hiden.pw'
GMODPORT = 27015
APRILFOOLS_2022 = False
APRILFOOLS_2023 = False
APRILFOOLS_2024 = False
ROLLOUT_MODE = False
CAT_API_KEY = ''
ENABLE_HBOT_APIS = False

# Import settings from settings_local.py. If settings_local.py is not present, terminate
try:
	from settings_local import *
except ImportError:
	raise Exception("settings_local.py not found, please create it.")