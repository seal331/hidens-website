import jinja2
import PyRSS2Gen
from aiohttp import web
from markupsafe import Markup
from datetime import datetime
import dateutil.parser
import json

import settings

def RunServ(serve_static = False, serve_storage = False, serve_js = False):
	app = App()

	# YanDev code g o

	app.router.add_get('/', page_index)
	app.router.add_get('/projects', page_projects)
	app.router.add_get('/places', page_places)
	app.router.add_get('/downloads', page_downloads)
	app.router.add_get('/downloads/software', page_downloads_software)
	app.router.add_get('/downloads/cursors', page_downloads_cursors)
	app.router.add_get('/downloads/software/winamp', page_winamp)
	app.router.add_get('/about', page_about)
	app.router.add_get('/about/socials', page_socials)
	app.router.add_get('/about/faq', page_faq)
	app.router.add_get('/computers', page_computers)
	app.router.add_get("/computers/desktops/a5ke4", page_computers_desktop_a5ke4)
	app.router.add_get("/computers/desktops/hpp23", page_computers_desktop_hpp23)
	app.router.add_get('/blog', page_blog)
	app.router.add_get('/blog/rss', blog_rss)
	app.router.add_get('/discord', page_discord)
	app.router.add_get('/discord/invite', page_discord_server_redir)
	app.router.add_get('/discord/rules', page_discord_rules)
	app.router.add_get('/services', page_services)
	app.router.add_get('/services/gamesrv', page_game_serv)
	app.router.add_get('/services/gamesrv/gmod', page_gmod)
	app.router.add_get('/services/gamesrv/gmod/addons', page_gmod_addons)
	app.router.add_get('/services/gamesrv/gmod/rules', page_gmod_rules)
	app.router.add_get('/services/gamesrv/mc', page_mc)
	app.router.add_get('/services/gamesrv/mc/latest', page_mc_latest)
	app.router.add_get('/services/gamesrv/mc/125', page_mc_125)
	app.router.add_get('/services/gamesrv/mc/b173', page_mc_b173)
	app.router.add_get('/services/gamesrv/mc/rules', page_mc_rules)
	app.router.add_get('/services/generalsrv', page_general_serv)
	app.router.add_get('/services/vms', page_vmlist)
	app.router.add_get('/projects/pubsite', page_pubsite_details)
	app.router.add_get('/projects/pubsite/ssg', page_pubsite_ssgallery)
	app.router.add_get('/projects/randomapp1', page_randomapp1_details)
	app.router.add_get('/projects/randomapp1/ssg', page_randomapp1_ssgallery)
	app.router.add_get('/projects/hbot', page_hbot_details)
	app.router.add_get('/projects/website', page_website_details)
	app.router.add_get('/projects/website/compatlist', page_website_compatlist)
	
	if settings.TESTING:
		print("Testing mode enabled! Test content (i.e: unfinished content and experiements) is served under /testing")
		app.router.add_get('/testing', page_testing)
		app.router.add_get('/testing/too', page_testing_too)

	#if not settings.TESTING:
	#	app.router.add_get('/foo/bar', page_nrfs)

	if settings.APRILFOOLS_2023:
		print("April Fools 2023 mode enabled!")
		app.router.add_get('/why', page_why_af23)

	if settings.APRILFOOLS_2022:
		print("April Fools 2022 mode enabled!")

	if settings.APRILFOOLS_2023 and settings.APRILFOOLS_2022:
		raise Exception("You can only have one holiday mode enabled. Terminating.")

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
	if settings.APRILFOOLS_2022:
		return render(req, 'index.aprilfools.2022.html')
	elif settings.APRILFOOLS_2023:
		return render(req, 'index.aprilfools.2023.html')
	else:
		return render(req, 'index.html')

	
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
		'title': 'AORUS 5 KE4 Desktop | My computers'
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
		'title': 'H-Bot | Projects'
	})

async def page_website_details(req):
	return render(req, 'projects.website.html', {
		'title': 'Website | Projects'
	})

async def page_website_compatlist(req): 
	return render(req, 'projects.website.compatlist.html', {
		'title': 'Compatibility list | Website | Projects'
	})

async def page_winamp(req):
	return render(req, 'winamp.html', {
		'title': 'Winamp selection'
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

async def page_nrfs(req):
	return render(req, 'nrfs.html', {    
		'title': 'NOT READY YET'
	})
	
async def page_blog(req):
	with open('json/posts.json', 'rb') as bp:
		bp_json = json.loads(bp.read())
		bp.close()
	
	entries = []
	
	for date, items in bp_json.items():
		tmpl = req.app.jinja_env.get_template('blog.post.item.html')
		items_markup = [tmpl.render(item = Markup(item)) for item in items]
		
		tmpl = req.app.jinja_env.get_template('blog.post.html')
		entries.append(tmpl.render(date = dateutil.parser.isoparse(date).strftime('%Y-%m-%d'), items = Markup('\n'.join(items_markup))))
	
	return render(req, 'blog.html', {
		'title': 'Blog',
		'entries': Markup('\n'.join(entries))
	})

async def blog_rss(req):
	with open('json/posts.json', 'rb') as bp:
		bp_json = json.loads(bp.read())
		bp.close()
	
	rss = PyRSS2Gen.RSS2(
		title = "HIDEN's Blog",
		link = "https://hiden.pw/blog",
		description = "My blog, where I post about... well... things.",
		generator = "PyRSS2Gen",
		docs = "https://validator.w3.org/feed/docs/rss2.html",
		language = "en-us",
		webMaster = "hiden64@protonmail.com",
		
		lastBuildDate = datetime.utcnow(),
		
		items = [
			PyRSS2Gen.RSSItem(
				title = dateutil.parser.isoparse(date).strftime('%Y-%m-%d'),
				description = ''.join(['{}\n'.format(entry) for entry in entries]),
				pubDate = dateutil.parser.isoparse(date),
			) for date, entries in bp_json.items()
		]
	)
	
	return web.Response(status = 200, content_type = 'text/xml', text = rss.to_xml(encoding = 'utf-8'))

async def handle_404(req):
	return render(req, '404.html', { 
		'title': 'Page not found' 
		}, status = 404
	)

def render(req, tmpl, ctxt = None, status = 200):
	tmpl = req.app.jinja_env.get_template(tmpl)
	if ctxt == None:
		ctxt = {}
	content = tmpl.render(**ctxt)
	return web.Response(status = status, content_type = 'text/html', text = content)