from aiohttp import web
from site_ctrl import RunServ
import logging 
import settings
import sys

def main():
	if sys.version_info < (3, 6):
		raise Exception("Unsupported Python version. Please use Python 3.6 or later.")

	app = RunServ()

	if settings.ENABLE_LOGGING:
		logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG) if settings.LOG_TO_FILE else logging.basicConfig(level=logging.DEBUG)
			
	web.run_app(app, port=settings.PORT)


if __name__ == '__main__':
	main()
