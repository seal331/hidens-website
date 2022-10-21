# Contributing to the site
This document provides ways on how you could countribute to the site.

## Running the server

### Requirements:
- Python 3.6 or newer
- pip
- Preferably a *nix environment, although Windows works too

### Installing the required packages
Install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, install it.

### Configuration
Create `settings_local.py`. The avaliable options are as follows:

`PORT`, What port shall the server run on. Change this to something else if on *nix (or run it as root), due to a permissions error.

`ENABLE_LOGGING`, Logs every connection to the server in the terminal ouput.

`LOG_TO_FILE`, Outputs the afformentioned connection logs to a file instead. You must set ENABLE_LOGGING to True as well to use this.

`TESTING`, Enables W.I.P. pages and experiements. Pretty much just an on/off toggle for running W.I.P./beta code. The pages are served under `/testing`.

`SERVE_STATIC`, Serves the `/static` directory (images, CSS stylesheets, old stuff).

`SERVE_STORAGE`, Serves the `/storage` directory (software, cursors).

`SERVE_JS`, Serves JavaScript content. 

`APRILFOOLS_2022`, Enables the April Fools day holiday page that was used in 2022.

`APRILFOOLS_2023`, Enables the April Fools day holiday page that will be used in 2023.

You must create `settings_local.py` to start the server. However, you do not need to add content the the file.

### Post-configuration
Once confiugration is done, run the server with `runserver.py`.

If you'd like to mimic [the production enviornment](https://hiden.pw), you can set up an Nginx reverse proxy. [Apache is not recommended for this use case.](https://github.com/aio-libs/aiohttp/issues/2687)

## Reporting issues

Please file any bugs you find in the `Issues` tab of this repository,  or contact me using the provided info at [/about/contact](https://hiden.pw/about/contact).

Here's an example template you could use:
```
OS: Some OS
Python ver: 3.XX.X
Using a reverse proxy?: yes/no
If yes, what web server?: Some web server
Post your settings_local.py file: Self explanatory
Descripition of the issue: Blah blah blah is not working
How do I reporduce the issue?: you do X and then Y and it breaks
(Screenshot and/or terminal output here)
```

To report an issue with the pages themselves, you can use this template:
```
OS: Some OS
Browser: Some Browser v1.0
What extensions are installed?: Foo the Bar v1.0
Type of device?: PC/phone/etc
Screen resolution: WxH
Description of the issue: blah blah is broken
(Screenshot here)
```
