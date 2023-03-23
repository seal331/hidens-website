import jinja2, json, settings, os, aiohttp
from aiohttp import web, request
from markupsafe import Markup
from datetime import datetime, timezone
from PyRSS2Gen import RSS2, RSSItem
from dateutil.parser import isoparse
from urllib.parse import parse_qs

def RunServ(serve_static=settings.SERVE_STATIC, serve_storage=settings.SERVE_STORAGE, serve_js=settings.SERVE_JS):
	app = App()

	get_routes = [
		('/', page_index),
		('/projects', page_projects),
		('/places', page_places),
		('/downloads', page_downloads),
		('/downloads/software', page_downloads_software),
		('/downloads/software/winamp', page_downloads_software_winamp),
		('/downloads/software/wmp', page_downloads_software_wmp),
		('/downloads/software/vpc', page_downloads_software_vpc),
		('/downloads/cursors', page_downloads_cursors),
		('/about', page_about),
		('/about/socials', page_socials),
		('/about/faq', page_faq),
		('/computers', page_computers),
		('/computers/desktops/a5ke4', page_computers_desktop_a5ke4),
		('/computers/desktops/hpp23', page_computers_desktop_hpp23),
		('/blog', page_blog),
		('/blog/rss', blog_rss),
		('/discord', page_discord),
		('/discord/invite', page_discord_server_redir),
		('/discord/rules', page_discord_rules),
		('/services', page_services),
		('/services/gamesrv', page_game_serv),
		('/services/gamesrv/gmod', page_gmod),
		('/services/gamesrv/gmod/addons', page_gmod_addons),
		('/services/gamesrv/gmod/rules', page_gmod_rules),
		('/services/gamesrv/mc', page_mc),
		('/services/gamesrv/mc/latest', page_mc_latest),
		('/services/gamesrv/mc/latest/status', page_mc_latest_status),
		('/services/gamesrv/mc/125', page_mc_125),
		('/services/gamesrv/mc/b173', page_mc_b173),
		('/services/gamesrv/mc/rules', page_mc_rules),
		('/services/generalsrv', page_general_serv),
		('/services/vms', page_vmlist),
		('/projects/pubsite', page_pubsite_details),
		('/projects/pubsite/ssg', page_pubsite_ssgallery),
		('/projects/randomapp1', page_randomapp1_details),
		('/projects/randomapp1/ssg', page_randomapp1_ssgallery),
		('/projects/hbot', page_hbot_details),
		('/projects/website', page_website_details),
		('/projects/website/compatlist', page_website_compatlist),
		('/guestbook', page_guestbook),
	]

	post_routes = [
		('/guestbook/submit', gb_submission_handler),
	]

	if settings.TESTING:
		print("Testing mode enabled! Test content (i.e: unfinished content and experiements) is served under /testing")
		get_routes += [
			('/testing', page_testing),
			('/testing/too', page_testing_too),
		]

	if settings.APRILFOOLS_2023:
		print("April Fools 2023 mode enabled!")
		get_routes.append(('/why', page_why_af23))

	if settings.APRILFOOLS_2022:
		print("April Fools 2022 mode enabled!")

	if settings.APRILFOOLS_2023 and settings.APRILFOOLS_2022:
		raise Exception("You can only have one holiday mode enabled. Terminating.")

	for route in get_routes:
		app.router.add_get(route[0], route[1])

	for route in post_routes:
		app.router.add_post(route[0], route[1])

	if serve_static:
		app.router.add_static('/static', 'static')
	if serve_storage:
		app.router.add_static('/storage', 'storage')
	if serve_js:
		app.router.add_static('/js', 'javascript')

	app.router.add_route('*', '/{path:.*}', handle_404)

	app.jinja_env = jinja2.Environment(
		loader = jinja2.FileSystemLoader('tmpl'),
		autoescape = jinja2.select_autoescape(default = True),
	)
	
	return app

	
class App(web.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

# YanDev code g o

async def page_index(req):
	context = {
		'settings': settings
	}
	return render(req, 'index.aprilfools.2023.html' if settings.APRILFOOLS_2023 else 'index.aprilfools.2022.html' if settings.APRILFOOLS_2022 else 'index.html', context)

	
async def page_projects(req):
	return render(req, 'projects.html', {
		'title': 'Projects'
	})
	
async def page_places(req):
	return render(req, 'places.html', {
		'title': 'Places'
	})

async def page_downloads(req):
	return render(req, 'downloads.html', {
		'title': 'Downloads'
	})

async def page_downloads_software(req):
	return render(req, 'downloads.software.html', {
		'title': 'Downloads | Software'
	})

async def page_downloads_software_winamp(req):
	return render(req, 'downloads.software.winamp.html', {
		'title': 'Winamp build selection'
	})

async def page_downloads_software_wmp(req):
	return render(req, 'downloads.software.wmp.html', {
		'title': 'WMP version selection'
	})

async def page_downloads_software_vpc(req):
	return render(req, 'downloads.software.vpc.html', {
		'title': 'Win8/10 install instructions | Virtual PC'
	})

async def page_downloads_cursors(req):
	return render(req, 'downloads.cursors.html', {
		'title': 'Downloads | Cursors'
	})

async def page_computers(req):
	return render(req, 'computers.html', {
		'title': 'My computers'
	})

async def page_computers_desktop_a5ke4(req):
	return render(req, 'computers.desktops.a5ke4.html', {
		'title': 'Gigabyte AORUS 5 KE4 Desktop | My computers'
	})

async def page_computers_desktop_hpp23(req):
	return render(req, 'computers.desktops.hpp23.html', {
		'title': 'HP Pavilion 23 Desktop | My computers'
	})

async def page_about(req):
	return render(req, 'about.html', {
		'title': 'About me'
	})

async def page_socials(req):
	return render(req, 'about.socials.html', {
		'title': 'Social/Messaging services | About me'
	})

async def page_faq(req):
	return render(req, 'about.faq.html', {
		'title': 'Frequently Asked Questions | About me'
	})
	
async def page_services(req):
	return render(req, 'services.html', {	
		'title': 'HIDNet services'
	})

async def page_vmlist(req):
	return render(req, 'services.vmlist.html', {	
		'title': 'Virtual Machine list | HIDNet services'
	})

async def page_game_serv(req):
	return render(req, 'services.gamesrv.html', {	
		'title': 'Game servers | HIDNet services'
	})
	
async def page_gmod(req):
	return render(req, 'services.gamesrv.gmod.html', {
		'title': 'Garry\'s Mod | Game servers | HIDNet services'
	})
	
async def page_gmod_addons(req):
	return render(req, 'services.gamesrv.gmod.addons.html', {
		'title': 'Garry\'s Mod addons | Game servers | HIDNet services'
	})
	
async def page_gmod_rules(req):
	return render(req, 'services.gamesrv.gmod.rules.html', {
		'title': 'Garry\'s Mod rules | Game servers | HIDNet services'
	})
	
async def page_mc(req):
	return render(req, 'services.gamesrv.mc.html', {
		'title': 'Minecraft server | Game servers | HIDNet services'
	})

async def page_mc_latest(req):
	return render(req, 'services.gamesrv.mc.latest.html', {
		'title': 'MC latest server | Game servers | HIDNet services'
	})

async def page_mc_latest_status(req):
	server_ip = settings.MCHOST
	server_port = settings.MCPORT
	
	try:
		# Attempt to connect to the Minecraft server
		async with aiohttp.ClientSession() as session:
			async with session.get(f'https://api.mcsrvstat.us/2/{server_ip}:{server_port}') as resp:
				if resp.status == 200:
					server_status = (await resp.json()).get('online', False)
				else:
					server_status = False
	except:
		server_status = False
	
	return render(req, 'services.gamesrv.mc.latest.status.html', {
		'title': 'MC latest server | Game servers | HIDNet services',
		'server_status': server_status
	})

async def page_mc_125(req):
	return render(req, 'services.gamesrv.mc.125.html', {
		'title': 'MC 1.2.5 server | Game servers | HIDNet services'
	})

async def page_mc_b173(req):
	return render(req, 'services.gamesrv.mc.b173.html', {
		'title': 'MC b1.7.3 server | Game servers | HIDNet services'
	})

async def page_mc_rules(req):
	return render(req, 'services.gamesrv.mc.rules.html', {
		'title': 'Minecraft rules | Game servers | HIDNet services'
	})

async def page_general_serv(req):
	return render(req, 'services.generalsrv.html', {	
		'title': 'General services | HIDNet services'
	})

async def page_discord(req):
	return render(req, 'discord.html', {
		'title': 'Discord server'
	})

async def page_discord_rules(req):
	return render(req, 'discord.rules.html', {
		'title': 'Rules | Discord server'
	})

async def page_discord_server_redir(req):
	return render(req, 'discord.serverredir.html', {
		'title': 'Invite link | Discord server'
	})
	
async def page_pubsite_details(req):
	return render(req, 'projects.pubsite.html', {
		'title': 'Pubsite | Projects'
	})
	
async def page_pubsite_ssgallery(req):
	return render(req, 'projects.pubsite.ssgallery.html', {
		'title': 'Screenshot Gallery | Pubsite | Projects'
	})

async def page_randomapp1_details(req):
	return render(req, 'projects.randomapp1.html', {
		'title': 'RandomApp1 | Projects'
	})

async def page_randomapp1_ssgallery(req):
	return render(req, 'projects.randomapp1.ssgallery.html', {
		'title': 'Screenshot Gallery | RandomApp1 | Projects'
	})

async def page_hbot_details(req):
	return render(req, 'projects.hbot.html', {
		'title': 'HBot | Projects'
	})

async def page_website_details(req):
	return render(req, 'projects.website.html', {
		'title': 'Website | Projects'
	})

async def page_website_compatlist(req): 
	return render(req, 'projects.website.compatlist.html', {
		'title': 'Compatibility list | Website | Projects'
	})

async def page_guestbook(req):
	entries = load_entries()
	reventeries = list(reversed(entries))
	banned_ips = load_banned_ips()

	if req.remote in banned_ips:
		return web.Response(text="You are not allowed to view or post to this guestbook as you've been banned. Email hiden64@protonmail.com for more details or to appeal your ban.")

	return render(req, 'guestbook.html', {
		'title': 'Guestbook',
		'entries': reventeries
	})

async def page_testing(req):
	return render(req, 'testing.html', {
		'title': 'Testing | Page 1'
	})

async def page_testing_too(req): 
	return render(req, 'testing.too.html', {
		'title': 'Testing | Page 2'
	})

async def page_why_af23(req): 
	return render(req, 'why.aprilfools.2023.html')

async def page_notready(req):
	return render(req, 'nrfs.html', {	
		'title': 'NOT READY YET'
	})
	
async def page_blog(req):
	with open('json/bp.json', 'rb') as bp:
		bp_json = json.load(bp)
	
	entries = []
	
	for date, items in bp_json.items():
		items_markup = [req.app.jinja_env.get_template('blog.post.item.html').render(item = Markup(item)) for item in items]
		entries.append(req.app.jinja_env.get_template('blog.post.html').render(date = isoparse(date).strftime('%Y-%m-%d'), items = Markup('\n'.join(items_markup))))
	
	return render(req, 'blog.html', {'title': 'Blog', 'entries': Markup('\n'.join(entries))})

async def blog_rss(req):
	with open('json/bp.json', 'rb') as bp:
		bp_json = json.load(bp)
	
	rss_items = [
		RSSItem (
			title=f"{isoparse(date).strftime('%Y-%m-%d')}",
			description = ''.join([f'{entry}\n' for entry in entries]),
			pubDate=isoparse(date).replace(tzinfo=timezone.utc),
		) for date, entries in bp_json.items()
	]

	rss = RSS2(
		title="HIDEN's Blog",
		link="https://hiden.pw/blog",
		description="My blog, where I post about... well... things.",
		generator="PyRSS2Gen",
		docs="https://validator.w3.org/feed/docs/rss2.html",
		language="en-us",
		webMaster="hiden64@protonmail.com",
		lastBuildDate=datetime.utcnow().replace(tzinfo=timezone.utc),
		items=rss_items,
	)

	return web.Response(status=200, content_type='text/xml', text=rss.to_xml(encoding='utf-8'))

async def handle_404(req):
	return render(req, '404.html', { 
		'title': 'Page not found' 
		}, status = 404
	)
	
async def gb_submission_handler(req):
	data = await req.post()
	name = data['name']
	email = data['email']
	message = data['message']
	location = data['location']
	website = data['website']

	add_entry(req.remote, name, email, location, website, message)

	return web.HTTPFound('/guestbook')

def load_entries():
	if not os.path.exists('json/gb.json'):
		return {}
	with open('json/gb.json', "r") as f:
		data = json.load(f)
		return data

def add_entry(ip_address, name, email, location, website, message):
	entries = load_entries()
	banned_ips = load_banned_ips()
	if ip_address in banned_ips:
		return web.Response(text="You are not allowed to view or post to this guestbook as you've been banned. Email hiden64@protonmail.com for more details or to appeal your ban.")

	new_entry = {
		"name": name,
		"email": email,
		"message": message,
		"location": location,
		"website": website,
		"date": datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
	}

	entries.append(new_entry)
	save_entries(entries)
	
def save_entries(entries):
	with open('json/gb.json', 'w') as f:
		json.dump(entries, f)

def load_banned_ips():
	if not os.path.exists('json/gb_bans.json'):
		return []
	with open ('json/gb_bans.json', 'r') as f:
		banned_ips = json.load(f)
		return banned_ips
	
def render(req, tmpl, ctxt=None, status=200):
	tmpl = req.app.jinja_env.get_template(tmpl)
	ctxt = ctxt or {}
	content = tmpl.render(**ctxt)
	return web.Response(text=content, content_type='text/html', status=status)