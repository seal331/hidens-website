from aiohttp import web
from site_ctrl import run_site

import settings

def main():
	app = run_site(serve_static = True)
	web.run_app(app, port = settings.PORT)

if __name__ == '__main__':
	main()