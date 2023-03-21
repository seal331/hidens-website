from aiohttp import web
from site_ctrl import RunServ
import logging, settings, sys, os


def main():
	gbjsonfile = "json/gb.json"

	print("Checking Guestbook JSON file integrity...")

	if not os.path.isfile(gbjsonfile):
		resp = input("gb.json not found, would you like to create it? (Y/n): ")
		if resp == "" or resp == "y":
			with open(gbjsonfile, "w") as f:
				f.write("{}")
				print("File created successfully.")
		elif resp == "n":
			print("File not created. The guestbook will not work unless you create the file!")
		else:
			print("Invalid option. Try again.")
			
	print("Check completed.")
	print("Starting server...")
	
	if sys.version_info < (3, 6):
		raise Exception("Unsupported Python version. Please use Python 3.6 or later.")

	app = RunServ()

	if settings.ENABLE_LOGGING:
		logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG) if settings.LOG_TO_FILE else logging.basicConfig(level=logging.DEBUG)
			
	web.run_app(app, port=settings.PORT)


if __name__ == '__main__':
	main()
