from aiohttp import web
from site_ctrl import RunServ
import logging 
import settings

def main(*, bool = False):

	app = RunServ(serve_static = settings.SERVE_STATIC, serve_storage = settings.SERVE_STORAGE, serve_js = settings.SERVE_JS)

	if settings.ENABLE_LOGGING:
		if settings.LOG_TO_FILE:
			logging.basicConfig (
				filename='log.txt',
				filemode='a',
				format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
				datefmt='%H:%M:%S',
				level=logging.DEBUG
			)
			
		else:
			logging.basicConfig(level=logging.DEBUG)

	if settings.USE_PORT:
		web.run_app(app, port = settings.PORT)
	elif settings.USE_SOCK:
		web.run_app(app, sock = settings.SOCK)
	else:
		raise Exception("Please set either USE_PORT or USE_SOCK to true in settings_local.py")


if __name__ == '__main__':
	main()