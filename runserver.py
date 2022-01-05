from aiohttp import web
from site_ctrl import run_site

import settings

# TODO: Add a logging feature

def main():
	# TODO: Fix HTTPS so that it detects the certificate files correctly
	if settings.ENABLE_HTTPS == True:
		from site_ctrl import ssl_context
		app = run_site(serve_static = True)
		web.run_app(app, ssl_context=ssl_context, port = settings.PORT)

	else:
		app = run_site(serve_static = True)
		web.run_app(app, port = settings.PORT)

if __name__ == '__main__':
	main()