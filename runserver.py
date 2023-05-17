import logging, os, sys
from aiohttp import web
from site_ctrl import RunServ
import settings

def main():
	if sys.version_info < (3, 7):
		raise Exception("Unsupported Python version. Please use Python 3.7 or later.")

	files = {
		"json/bp.json": "bp.json not found, would you like to create it? (Y/n): ",
		"json/gb.json": "gb.json not found, would you like to create it? (Y/n): ",
		"json/gb_bans.json": "gb_bans.json not found, would you like to create it? (Y/n): ",
	}

	print("Checking file integrity...")

	for filename, prompt_msg in files.items():
		if not os.path.isfile(filename):
			resp = input(prompt_msg)
			if resp.lower() in {"y", ""}:
				with open(filename, "w") as f:
					f.write("[]")
				print(f"{filename} created successfully.")
			elif resp.lower() == "n":
				print(f"{filename} not created. Things will break, beware!")
			else:
				print("Invalid option. Try again.")

	print("Check completed.")
	print("Starting server...")

	app = RunServ()

	if settings.ENABLE_LOGGING:
		log_format = (
			"%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
		)
		logging.basicConfig(
			filename="access.log",
			filemode="a",
			format=log_format,
			datefmt="%H:%M:%S",
			level=logging.DEBUG,
		) if settings.LOG_TO_FILE else logging.basicConfig(level=logging.DEBUG)

	web.run_app(app, port=settings.PORT)


if __name__ == "__main__":
	main()
