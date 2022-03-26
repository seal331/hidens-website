import jinja2
import PyRSS2Gen
from aiohttp import web
from markupsafe import Markup
from datetime import datetime, timedelta
import dateutil.parser
import json

import settings

def RunServ(*, serve_static = False, serve_storage = False, serve_js = False):
	app = App()

	# YanDev code g o

	app.router.add_get('/', page_index)
	app.router.add_get('/projects', page_projects)
	app.router.add_get('/links', page_links)
	app.router.add_get('/downloads', page_downloads)
	app.router.add_get('/downloads/software', page_downloads_software)
	app.router.add_get('/downloads/cursors', page_downloads_cursors)
	app.router.add_get('/about', page_about_me)
	app.router.add_get('/computers', page_my_computers)
	app.router.add_get('/gamesrv', page_game_srv)
	app.router.add_get('/gamesrv/mc', page_mc_srv)
	app.router.add_get('/gamesrv/mc/rules', page_mc_srv_rules)
	app.router.add_get('/gamesrv/mc/plugins', page_mc_srv_plugins)
	app.router.add_get('/gamesrv/tf2', page_tf2_srv)
	app.router.add_get('/gamesrv/tf2/rules', page_tf2_srv_rules)
	app.router.add_get('/news', page_news)
	app.router.add_get('/news/rss', rss_news)
	

	if settings.TESTING:
		app.router.add_get('/testing', page_testing)
		app.router.add_get('/testing/too', page_testing_too)

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
	return render(req, 'index.html')

async def page_projects(req):
	return render(req, 'projects.html', {
		'title': 'Projects'
	})

async def page_links(req):
	return render(req, 'links.html', {
		'title': 'Links'
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

async def page_about_me(req):
	return render(req, 'about.me.html', {
		'title': 'About me'
	})

async def page_game_srv(req):
	return render(req, 'game.servers.html', {
		'title': 'My game servers'
	})

async def page_mc_srv(req):
	return render(req, 'minecraft.srv.html', {
		'title': 'Minecraft server'
	})

async def page_mc_srv_rules(req):
	return render(req, 'minecraft.rules.html', {
		'title': 'Minecraft rules',
	})

async def page_mc_srv_plugins(req):
	return render(req, 'minecraft.plugins.html', {
		'title': 'Minecraft plugins',
	})

async def page_tf2_srv(req):
	return render(req, 'tf2.srv.html', {
		'title': 'Team Fortress 2 server'
	})

async def page_tf2_srv_rules(req):
	return render(req, 'tf2.rules.html', {
		'title': 'TF2 rules'
	})

async def page_news(req):
	with open('json/news.json', 'rb') as news:
		news_json = json.loads(news.read())
		news.close()
	
	entries = []
	
	for date, items in news_json.items():
		tmpl = req.app.jinja_env.get_template('news.entry.item.html')
		items_markup = [tmpl.render(item = Markup(item)) for item in items]
		
		tmpl = req.app.jinja_env.get_template('news.entry.html')
		entries.append(tmpl.render(date = dateutil.parser.isoparse(date).strftime('%Y-%m-%d'), items = Markup('\n'.join(items_markup))))
	
	return render(req, 'news.html', {
		'title': 'News',
		'entries': Markup('\n'.join(entries))
	})

async def rss_news(req):
	with open('json/news.json', 'rb') as news:
		news_json = json.loads(news.read())
		news.close()
	
	rss = PyRSS2Gen.RSS2(
		title = "HIDEN's RSS Feed",
		link = "https://hiden64.ddns.net/news",
		description = "News about my website, projects, and whatever's on my mind.",
		docs = "",
		
		lastBuildDate = datetime.utcnow(),
		
		items = [
			PyRSS2Gen.RSSItem(
				title = dateutil.parser.isoparse(date).strftime('%Y-%m-%d'),
				description = ''.join(['{}\n'.format(entry) for entry in entries]),
				pubDate = dateutil.parser.isoparse(date),
			) for date, entries in news_json.items()
		]
	)
	
	return web.Response(status = 200, content_type = 'text/xml', text = rss.to_xml(encoding = 'utf-8'))

if settings.TESTING:
	async def page_testing(req):
		return render(req, 'testing.html', {
			'title': 'Testing | Page 1'
 		})

	async def page_testing_too(req): 
		return render(req, 'testing.too.html', {
			'title': 'Testing | Page 2'
		})

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

