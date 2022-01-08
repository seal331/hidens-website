# HIDEN's personal website
This the source code to my personal website, which you can find at http://hiden.ooguy.com.

To run, install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, install it from your distibution's package manager assuming you're running Linux. The Windows/macOS version of Python should come with pip installed by default.

Then, create `settings_local.py`, and add the following options:

```
PORT = 80 (Default is 80, change it to something else if you want to)
ENABLE_HTTPS = False (Default is False. Currently nonfunctional for unknown reasons, but this is supposed to enable HTTPS support)
SERVE_STATIC = False (Default is false. If you want to serve static content such as CSS stylesheets or images, set this to True)
SERVE_STORAGE = False (Default is false. If you want to serve items in storage such as installers, set this to True)
```

After that, run the site with "python runserver.py".
