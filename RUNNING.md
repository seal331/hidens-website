# Getting the server up and running
This document provides instructions on how to run the server.

## Requirements:
- Python 3.6 or newer is required, the server may work on older versions but these versions are what it has been tested with
- pip; Should be installed by default on Windows, install it with your distrubition's package manager on Linux, install it on macOS with [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
- A *nix environment is preferred, but it has been tested to work with Windows too
- An Nginx reverse proxy is recommended for production enviornments, however it is not needed for development enviornments

## Running:
To run, install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, check requirement #2 above.

Then, create `settings_local.py`, and add the following options as :

 ```
PORT = 80 (On *nix, this causes a permissions error if not ran as root, change the port or run it as root to resolve this)

ENABLE_LOGGING = False (Logs every connection to the server in the terminal ouput. Set this to True if you want this)

LOG_TO_FILE = False (Set this to true and ENABLE_LOGGING to true if you want to output connection and process logs to a file)

TESTING = False (Set this to true if you want to view stuff that's in development, and experiements that I'm screwing around with, once that's enabled, go to /testing)

SERVE_STATIC = False (If you want to serve static content such as CSS stylesheets or images, set this to True)

SERVE_STORAGE = False (If you want to serve items in storage such as installers, set this to True)

SERVE_JS = False (Some experiements on the afformentioned testing pages will be disabled if this is left on False, so set it to True if you want to enable those)

```

Creating `settings_local.py` is required, but adding content to the file is optional. If `settings_local.py` is blank, then the server uses what's listed in `settings.py` instead.

After that, run the site with `python runserver.py`.

Please file any bugs you find in the Issues tab of this repository.<!--,  or contact me using the provided info [here](https://hiden.pw/about/contact), so I can more easily find and fix them.-->