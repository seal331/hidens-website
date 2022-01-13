from aiohttp import web
from site_ctrl import run_site, ssl_context
import logging 
import settings

def main(*, bool = False):
	
	# Start an aiohttp instance
	app = run_site(serve_static = settings.SERVE_STATIC, serve_storage = settings.SERVE_STORAGE)

	# Import ssl_context from site_ctrl if HTTPS is enabled
	if settings.ENABLE_HTTPS:
		# TODO: Find a more efficient way of running with HTTPS enabled, hopefully without calling run_site for a second time
		app = run_site(serve_static = settings.SERVE_STATIC, ssl_context=ssl_context, serve_storage = settings.SERVE_STORAGE)

	# Log requests to console if logging is enabled
	if settings.ENABLE_LOGGING:
		logging.basicConfig(level=logging.DEBUG)

	# Serve the aiohttp instance on the defined port
	web.run_app(app, port = settings.PORT)

if __name__ == '__main__':
	main()