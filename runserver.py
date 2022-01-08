from aiohttp import web
from site_ctrl import run_site, ssl_context
import logging 
import settings

def main(*, bool = False):
	app = run_site(serve_static = settings.SERVE_STATIC, serve_storage = settings.SERVE_STORAGE)
	if settings.ENABLE_HTTPS:
		app = run_site(serve_static = settings.SERVE_STATIC, ssl_context=ssl_context, serve_storage = settings.SERVE_STORAGE)
	if settings.ENABLE_LOGGING:
		logging.basicConfig(level=logging.DEBUG)
	web.run_app(app, port = settings.PORT)

if __name__ == '__main__':
	main()