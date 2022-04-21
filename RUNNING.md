# Running the server
This document describes instructions on how to start the server, and what it requires.

## Requirements:
- Python 3 (tested to work with 3.6 - 3.10, may not work with other versions)
- pip (Installed by default on Windows, install it with your distrubition's package manager on Linux, unsure about macOS)
- A *nix environment is preferred as the live instance uses Ubuntu, but it has been tested to work with Windows too


## Running:
To run, install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, check requirement #2 above.

Then, create `settings_local.py`, and add the following options:

 ```
PORT = 80 (Default is 80. Enable USE_PORT to use it. Change it to something else if you want to)

SOCK = "SET/SOMETHING/HERE" (Enable USE_SOCK to use it. Change it to the path of your Unix sock.)

ENABLE_LOGGING = False (Default is false. Logs every connection to the server in the terminal ouput. Set this to true if you want this.)

LOG_TO_FILE = False (Default is false. Set this to true and ENABLE_LOGGING to true if you want to output connection and process logs to a file.)

TESTING = False (Default is false. Set this to true if you want to view stuff that's in development, and experiements that I'm screwing around with.)

SERVE_STATIC = False (Default is false. If you want to serve static content such as CSS stylesheets or images, set this to True)

SERVE_STORAGE = False (Default is false. If you want to serve items in storage such as installers, set this to True)

SERVE_JS = False (Default is false. Some functions of the website will be disabled if this is left on False, so set it to True if you want to enable those)

```

Creating `settings_local.py` is mandatory, but adding content to the file is optional. If `settings_local.py` is blank, then the server uses the default settings.


After that, run the site with `python runserver.py`.

Please file any bugs you find in the "Issues" tab of this repository, or contact me using the provided info on the "about" page, so I can more easily find and patch them.