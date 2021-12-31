# HIDEN's personal website
This the source code to my personal website, which you can find at https://hiden.ooguy.com.

To run, install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, install it from your distibution's package manager assuming you're running Linux. The Windows version of Python should come with pip installed by default.

Then, create `settings_local.py`, and add the following options:

```
PORT = 80 (Default is 80, change it to something else if you want to)
ENABLE_HTTPS = False (Default is False. If you want HTTPS, change this to true)

```

After that, run the site with "python runserver.py".
