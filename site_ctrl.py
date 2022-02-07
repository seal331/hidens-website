import jinja2
import json
import PyRSS2Gen
from aiohttp import web
from markupsafe import Markup
from datetime import datetime, timedelta
import dateutil.parser
from markupsafe import Markup
import ssl
from typing import Dict, Tuple, Any, Optional
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.backends import default_backend as secure_backend

import settings

def RunServ(*, serve_static = False, serve_storage = False, serve_js = False):
	app = App()

	# YandereDev code g o

	app.router.add_get('/', page_index)
	app.router.add_get('/news', page_news)
	app.router.add_get('/news/rss', rss_news)
	app.router.add_get('/projects', page_projects)
	app.router.add_get('/links', page_links)
	app.router.add_get('/downloads', page_downloads)
	app.router.add_get('/favorite', page_favorite_stuff)
	app.router.add_get('/favorite/windowsranking', page_windows_ranking)
	app.router.add_get('/favorite/linux', page_favorite_linux)
	app.router.add_get('/favorite/software', page_favorite_misc_software)
	app.router.add_get('/favorite/music', page_favorite_music)
	app.router.add_get('/about', page_about_me)
	app.router.add_get('/computers', page_my_computers)
	app.router.add_get('/gamesrv', page_game_srv)
	app.router.add_get('/gamesrv/mc', page_mc_srv)
	app.router.add_get('/gamesrv/mc/rules', page_mc_srv_rules)
	app.router.add_get('/gamesrv/tf2', page_tf2_srv)
	app.router.add_get('/gamesrv/tf2/rules', page_tf2_srv_rules)
	app.router.add_get('/gamesrv/tf2/map', page_tf2_map_rotate)

	if settings.ENABLE_TESTPAGE:
		app.router.add_get('/testing', page_testpage)

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


# YandereDev code g o

async def page_index(req):
	return render(req, 'index.html')

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

async def page_my_computers(req):
	return render(req, 'computers.html', {
		'title': 'My computers'
	})

async def page_favorite_stuff(req):
	return render(req, 'favorite.html', {
		'title': 'My favorite stuff'
	})

async def page_windows_ranking(req):
	return render(req, 'favorite.windows.ranking.html', {
		'title': 'What I think about versions of Windows'
	})

async def page_favorite_linux(req):
	return render(req, 'favorite.oses.linux.html', {
		'title': 'My favorite Linux distributions'
	})

async def page_favorite_misc_software(req):
	return render(req, 'favorite.software.misc.html', {
		'title': 'My favorite miscellaneous software'
	})
	
async def page_favorite_music(req):
	return render(req, 'favorite.music.html', {
		'title': 'My favorite web music generes/artists'
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

async def page_tf2_srv(req):
	return render(req, 'tf2.srv.html', {
		'title': 'Team Fortress 2 server'
	})

async def page_tf2_srv_rules(req):
	return render(req, 'tf2.rules.html', {
		'title': 'TF2 rules'
	})

async def page_tf2_map_rotate(req):
	return render(req, 'tf2.map.rotate.html', {
		'title': 'TF2 map rotation'
	})	

if settings.ENABLE_TESTPAGE:
	async def page_testpage(req):
		return render(req, 'testing.html', {
			'title': 'Testing'
 		})

async def handle_404(req):
	return render(req, '404.html', { 
		'title': 'Page not found' 
		}, status = 404
	)

async def rss_news(req):
	with open('json/news.json', 'rb') as news:
		news_json = json.loads(news.read())
		news.close()
	
	rss = PyRSS2Gen.RSS2(
		title = "HIDEN's RSS Feed",
		link = "https://hiden64.duckdns.org/news",
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


# Haven't verfied that this works yet, will test it when I stop being lazy

if not settings.ENABLE_HTTPS:
	ssl_context = None

class TLSContext:
	def __init__(self, cert_root: str, cert_dir: str) -> None:
		self.cert_dir = Path(cert_dir)
		self.cert_root = cert_root
		self._cert_cache = {} # type: Dict[str, ssl.SSLContext]
	
	def create_ssl_context(self) -> ssl.SSLContext:
		self._get_root_cert()
		
		ssl_context = ssl.create_default_context(purpose = ssl.Purpose.CLIENT_AUTH)
		
		cache = self._cert_cache
		def servername_callback(socket: Any, domain: Optional[str], ssl_context: ssl.SSLSocket) -> Optional[int]:
			if domain is None:
				domain = 'no-domain'
			if domain not in cache:
				ctxt = ssl.create_default_context(purpose = ssl.Purpose.CLIENT_AUTH)
				p_crt, p_key = self._get_cert(domain)
				ctxt.load_cert_chain(str(p_crt), keyfile = str(p_key))
				cache[domain] = ctxt
			socket.context = cache[domain]
			return None
		
		ssl_context.set_servername_callback(servername_callback)
		return ssl_context
	
	def _get_cert(self, domain: str) -> Tuple[Path, Path]:
		p_crt = self.cert_dir / '{}.crt'.format(domain)
		p_key = self.cert_dir / '{}.key'.format(domain)
		
		if not exists_and_valid(p_crt, p_key):
			raise ssl.CertificateError()
		
		return p_crt, p_key
	
	def _get_root_cert(self) -> Tuple[Path, Path]:
		assert self.cert_root is not None
		
		p_crt = self.cert_dir / '{}.crt'.format(self.cert_root)
		p_key = self.cert_dir / '{}.key'.format(self.cert_root)
		
		if not exists_and_valid(p_crt, p_key):
			raise ssl.CertificateError()
		
		return p_crt, p_key

def exists_and_valid(p_crt: Path, p_key: Path) -> bool:
	if not p_crt.exists(): return False
	if not p_key.exists(): return False
	backend = secure_backend()
	with p_crt.open('rb') as fh:
		crt = x509.load_pem_x509_certificate(fh.read(), backend)
	
	now = datetime.utcnow()
	if now < crt.not_valid_before: return False
	near_future = now + timedelta(days = 1)
	if near_future > crt.not_valid_after: return False
	return True

def render(req, tmpl, ctxt = None, status = 200):
	tmpl = req.app.jinja_env.get_template(tmpl)
	if ctxt is None:
		ctxt = {}
	content = tmpl.render(**ctxt)
	return web.Response(status = status, content_type = 'text/html', text = content)

