from aiohttp import web
from site_ctrl import RunServ
import logging, settings, sys, os

def main():
		
	if sys.version_info < (3, 7):
		raise Exception("Unsupported Python version. Please use Python 3.7 or later.")
		
	def create_json_file(filename, prompt_msg, success_msg):
		if not os.path.isfile(filename):
			resp = input(prompt_msg)
			if resp == "" or resp.lower() == "y":
				with open(filename, "w") as f:
					f.write("[]")
					print(success_msg)
			elif resp.lower() == "n":
				print(f"File not created. Things will break, beware!")
			else:
				print("Invalid option. Try again.")

	json_files = {
		"json/gb.json": ("gb.json not found, would you like to create it? (Y/n): ", "File created successfully."),
		"json/gb_bans.json": ("gb_bans.json not found, would you like to create it? (Y/n): ", "File created successfully.")
	}

	print("Checking JSON file integrity...")

	for filename, messages in json_files.items():
		prompt_msg, success_msg = messages
		create_json_file(filename, prompt_msg, success_msg)
			
	print("Check completed.")
	print("Starting server...")

	app = RunServ()

	if settings.ENABLE_LOGGING:
		logging.basicConfig(filename='aiohttp.log', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG) if settings.LOG_TO_FILE else logging.basicConfig(level=logging.DEBUG)
			
	web.run_app(app, port=settings.PORT)


if __name__ == '__main__':
	main()
