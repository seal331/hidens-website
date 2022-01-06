from aiohttp import web
from site_ctrl import run_site
import sys
import logging 
import settings

def main(*, bool = False):
	app = run_site(serve_static = True)
	logging.basicConfig(level=logging.DEBUG)
	web.run_app(app, port = settings.PORT)
	# TODO: Fix HTTPS so that it detects the certificate files correctly

	if settings.ENABLE_HTTPS == True:
		from site_ctrl import ssl_context
		ssl_context=ssl_context

# TODO: Make logging optional
#	if settings.ENABLE_LOGGING == True:
#		import logging 
#		logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
	main()