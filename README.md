# HIDEN's personal website
This is the source code to my personal website, which you can find at https://hiden.pw. Because why not, as well as a reference point for an aiohttp+jinja2 website.

## Usage instructions

### Requirements:
- Python 3.7 or newer
- pip
- Preferably a *nix environment, although Windows works too

#### Officially supported OSes:
- Windows 7 or newer
- macOS 10.6 or newer
- Debian 9 or newer
- Ubuntu 18.04 or newer
- Fedora 29 or newer
- Any other Linux distribution that supports Python 3.7+

You will not receive technical assistance if you are using an unsupported OS, or if you're using a workaround to run this on an unsupported OS (such as Cygwin on older versions of Windows.)

### Installing the required packages
Install the requirements using pip: `pip install -r requirements .txt`. If you don't have pip, install it.

### Configuration
Create `settings_local.py`. The avaliable options are as follows:

`PORT`: The port that the server will use. Change this to something else if you already have something running on port 80, or if you do not have root privileges on *nix.

`ENABLE_LOGGING`: Logs every connection to the server in the terminal ouput.

`LOG_TO_FILE`: Outputs the afformentioned connection logs to a file instead. You must set `ENABLE_LOGGING` to `True` as well to use this.

`DEV_MODE`: Enables W.I.P. and/or experiemental content. The content is served at `/dev`. **NOTE FOR DEVELOPERS**: Enabling this is highly recommended.

`MCHOST`: What host to try for the Minecraft server.

`MCPORT`: What port the afformentioned host is using for the Minecraft server.

`GMODHOST`: What host to try for the Garry's Mod server.

`GMODPORT`: What port the afformentioned host is using for the Garry's Mod server.

`SERVE_STATIC`: Serves the `/static` directory (images, CSS stylesheets, old stuff).

`SERVE_STORAGE`: Serves the `/storage` directory (software, cursors).

`SERVE_JS`: Serves JavaScript content. 

`APRILFOOLS_2022`: Enables the April Fools day holiday page that was used in 2022.

`APRILFOOLS_2023`: Enables the April Fools day holiday page was intended to be used in 2023, but was cancelled due to a tornado hitting my city at the time.

`APRILFOOLS_2024`: Enables the April Fools day holiday page that will be used in 2024.

`ENABLE_HBOT_APIS`: Enables APIs used by HBot.

`CAT_API_KEY`: Used for supplying an API key for the cat API.

You must create `settings_local.py` to start the server. However, you do not need to add content the the file. If the file is empty, the default options in `settings.py` will be used instead.

### Post-configuration
Once configuration is done, start the server with `runserver.py`.

If you'd like to mimic [the production enviornment](https://hiden.pw), you may set up an NGINX reverse proxy. Caddy works too, although [Apache does not](https://github.com/aio-libs/aiohttp/issues/2687). The one I personally recommend most is NGINX.

After this, you should be ready to go!

## Tackling things

Stuck on what exactly you want to add and/or fix? There is a list of [things that are wanted](WANTED.md) that would greatly help development. Why not start with some? :P

## Reporting problems

If you encounter any issues/bugs, put them in the `Issues` tab of this repository, or shoot me a message at one of the services listed at [/about/socials](https://hiden.pw/about/socials).

Here's an example template you could use (intended for an issue with the backend):
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
