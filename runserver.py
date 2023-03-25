from aiohttp import web
from site_ctrl import RunServ
import logging, settings, sys, os

def main():
		
	if sys.version_info < (3, 6):
		raise Exception("Unsupported Python version. Please use Python 3.6 or later.")

	gbjsonfile = "json/gb.json"
	gbbansjsonfile = "json/gb_bans.json"

	print("Checking Guestbook JSON file integrity...")

	# I need to call this multiple times because you can't add more than one positional argumenet to os.path.isfile, 
	# TLDR: spaghetti code induced by Python bs
	# I also could theoretically just use 'and', but I'm too lazy to rewrite this accordingly right now

	if not os.path.isfile(gbjsonfile):
		resp = input("gb.json not found, would you like to create it? (Y/n): ")
		if resp == "" or resp == "y":
			with open(gbjsonfile, "w") as f:
				f.write("[]")
				print("File created successfully.")
		elif resp == "n":
			print("File not created. The guestbook will not work unless you create the file!")
		else:
			print("Invalid option. Try again.")

	if not os.path.isfile(gbbansjsonfile):
		resp = input("gb_bans.json not found, would you like to create it? (Y/n): ")
		if resp == "" or resp == "y":
			with open(gbbansjsonfile, "w") as f:
				f.write("[]")
				print("File created successfully.")
		elif resp == "n":
			print("File not created. You will not be able to ban people from the Guestbook without this!")
		else:
			print("Invalid option. Try again.")
			
	print("Check completed.")
	print("Starting server...")

	app = RunServ()

	if settings.ENABLE_LOGGING:
		logging.basicConfig(filename='aiohttp.log', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG) if settings.LOG_TO_FILE else logging.basicConfig(level=logging.DEBUG)
			
	web.run_app(app, port=settings.PORT)


if __name__ == '__main__':
	main()
