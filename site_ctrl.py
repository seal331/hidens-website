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
	app.router.add_get('/about', page_about)
	app.router.add_get('/about/contact', page_contact)
	app.router.add_get('/computers', page_my_computers)
	app.router.add_get('/mcsrv', page_mc_srv)
	app.router.add_get('/mcsrv/rules', page_mc_srv_rules)
	app.router.add_get('/mcsrv/plugins', page_mc_srv_plugins)
	app.router.add_get('/blog', page_blog)
	app.router.add_get('/blog/rss', blog_rss)
	app.router.add_get('/discord', page_discord_server_redir)
	app.router.add_get('/projects/pubsite', page_pubsite_details)
	app.router.add_get('/projects/pubsite/ssg', page_pubsite_ssgallery)
	app.router.add_get('/projects/randomapp1', page_randomapp1_details)
	app.router.add_get('/projects/randomapp1/ssg', page_randomapp1_ssgallery)
	app.router.add_get('/projects/hbot', page_hbot_details)
	app.router.add_get('/projects/website', page_website_details)
	
	if settings.TESTING:
		app.router.add_get('/testing', page_testing)
		app.router.add_get('/testing/too', page_testing_too)
		app.router.add_get('/testing/music', page_music)
		app.router.add_get('/testing/music/metallica', page_music_metallica)
		app.router.add_get('/testing/spam', page_spam)

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
	if settings.APRILFOOLS:
		return render(req, 'index.aprilfools.html')
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

async def page_my_computers(req):
	return render(req, 'computers.html', {
		'title': 'My computers'
	})

async def page_about(req):
	return render(req, 'about.html', {
		'title': 'About me'
	})

async def page_contact(req):
	return render(req, 'about.contact.html', {
		'title': 'Contact info | About me'
	})

async def page_mc_srv(req):
	return render(req, 'minecraft.srv.html', {
		'title': 'MC server'
	})

async def page_mc_srv_rules(req):
	return render(req, 'minecraft.rules.html', {
		'title': 'MC rules',
	})

async def page_mc_srv_plugins(req):
	return render(req, 'minecraft.plugins.html', {
		'title': 'MC plugins',
	})

async def page_discord_server_redir(req):
	return render(req, 'discord.html', {
		'title': 'Discord server',
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
	
async def page_music(req):
	return render(req, 'music.html', {
		'title': 'Home | Music'
	})

async def page_music_metallica(req):
	return render(req, 'music.metallica.html', {
		'title': 'Metallica | Music'
	})

async def page_spam(req):
	return render(req, 'spam.html', {
		'title': 'Spam'
	})
	
async def page_testing(req):
	return render(req, 'testing.html', {
		'title': 'Testing | Page 1'
	})

async def page_testing_too(req): 
	return render(req, 'testing.too.html', {
		'title': 'Testing | Page 2'
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
	if ctxt is None:
		ctxt = {}
	content = tmpl.render(**ctxt)
	return web.Response(status = status, content_type = 'text/html', text = content)

