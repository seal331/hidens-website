import jinja2
import json
import PyRSS2Gen
from aiohttp import web
from markupsafe import Markup
from datetime import datetime
import dateutil.parser
from markupsafe import Markup
import ssl

import settings

def run_site(*, serve_static = False, serve_storage = False):
	app = App()

	app.router.add_get('/', page_index)
	app.router.add_get('/news', page_news)
	app.router.add_get('/news/rss', rss_news)
	app.router.add_get('/projects', page_projects)
	app.router.add_get('/links', page_links)
	if serve_static:
		app.router.add_static('/static', 'static')
	if serve_storage:
		app.router.add_static('/storage', 'storage')
	app.router.add_route('*', '/{path:.*}', handle_404)
	app.jinja_env = jinja2.Environment(
		loader = jinja2.FileSystemLoader('tmpl'),
		autoescape = jinja2.select_autoescape(default = True),
	)
	return app

class App(web.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

async def page_index(req):
	return render(req, 'index.html', {
		'title': 'Homepage'
	})

async def page_news(req):
	with open('json/news.json', 'rb') as f:
		news_json = json.loads(f.read())
		f.close()
	
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

async def page_projects(req):
	return render(req, 'projects.html', {
		'title': 'Projects'
	})

async def page_links(req):
	return render(req, 'links.html', {
		'title': 'Links'
	})

async def handle_404(req):
	return render(req, '404.html', { 
		'title': 'Page not found' 
		}, status = 404
	)

async def rss_news(req):
	with open('json/news.json', 'rb') as f:
		news_json = json.loads(f.read())
		f.close()
	
	rss = PyRSS2Gen.RSS2(
		title = "HIDEN's RSS Feed",
		link = "https://hiden.ooguy.com/news",
		description = "The latest news on HIDEN's website.",
		docs = "",
		
		lastBuildDate = datetime.utcnow(),
		
		items = [
			PyRSS2Gen.RSSItem(
				title = dateutil.parser.isoparse(date).strftime('%Y-%m-%d'),
				description = ''.join(['<li>{}</li>\n'.format(entry) for entry in entries]),
				pubDate = dateutil.parser.isoparse(date),
			) for date, entries in news_json.items()
		]
	)
	
	return web.Response(status = 200, content_type = 'text/xml', text = rss.to_xml(encoding = 'utf-8'))

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
if settings.ENABLE_HTTPS:
	ssl_context.load_cert_chain('domain_srv.crt', 'domain_srv.key')

def render(req, tmpl, ctcx = None, status = 200):
	tmpl = req.app.jinja_env.get_template(tmpl)
	content = tmpl.render(**ctcx)
	return web.Response(status = status, content_type = 'text/html', text = content)