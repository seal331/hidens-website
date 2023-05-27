import jinja2, json, settings, os, aiohttp, asyncio, a2s, socket, base64, PyRSS2Gen
from aiohttp import web
from aiohttp.web import Request
from aiohttp.web_exceptions import HTTPBadRequest
from datetime import datetime, date

async def forward_headers_middleware(app, handler):
	async def middleware_handler(request):
		headers = request.headers.copy()
		real_ip = headers.get('X-Real-IP', request.remote)
		x_forwarded_for = headers.get('X-Forwarded-For', '')
		if x_forwarded_for:
			x_forwarded_for += ', '
		headers['X-Forwarded-For'] = x_forwarded_for + real_ip
		request = request.clone(headers=headers)
		return await handler(request)

	return middleware_handler

def RunServ(serve_static=settings.SERVE_STATIC, serve_storage=settings.SERVE_STORAGE, serve_js=settings.SERVE_JS):
	app = App(middlewares=[forward_headers_middleware])

	get_routes = [
		('/', page_index),
		('/projects', page_projects),
		('/projects/pubsite', page_pubsite_details),
		('/projects/pubsite/ssg', page_pubsite_ssgallery),
		('/projects/randomapp1', page_randomapp1_details),
		('/projects/randomapp1/ssg', page_randomapp1_ssgallery),
		('/projects/hbot', page_hbot_details),
		('/projects/website', page_website_details),
		('/projects/website/compatlist', page_website_compatlist),
		('/projects/autos', page_autos_details),
		('/places', page_places),
		('/places/friends', page_friendsplaces),
		('/places/misc', page_miscplaces),
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
		('/blog', page_blog),
		('/blog/post/{post_id:\d+}', blog_post),
		('/blog/rss.xml', blog_rss),
		('/discord', page_discord),
		('/discord/invite/link', page_discord_server_redir),
		('/discord/invite', page_discord_server_invite),
		('/discord/rules', page_discord_rules),
		('/services', page_services),
		('/services/gamesrv', page_game_serv),
		('/services/gamesrv/gmod', page_gmod),
		('/services/gamesrv/gmod/addons', page_gmod_addons),
		('/services/gamesrv/gmod/rules', page_gmod_rules),
		('/services/gamesrv/gmod/status', page_gmod_status),
		('/services/gamesrv/mc', page_mc),
		('/services/gamesrv/mc/latest', page_mc_latest),
		('/services/gamesrv/mc/latest/status', page_mc_latest_status),
		('/services/gamesrv/mc/125', page_mc_125),
		('/services/gamesrv/mc/b173', page_mc_b173),
		('/services/gamesrv/mc/rules', page_mc_rules),
		('/services/generalsrv', page_general_serv),
		('/services/vms', page_vmlist),
		('/guestbook', page_guestbook),
		('/api/hbot/check-update', hbot_check_update),
		('/api/hbot/random-cat', hbot_random_cat),
	]

	post_routes = [
		('/guestbook/submit', gb_submission_handler),
		('/blog/post/{post_id:\d+}', blog_comment),
	]

	if settings.DEV_MODE:
		print("Development mode enabled! Experiements and W.I.P. content is served under /dev")
		get_routes += [
			('/dev', page_development),
			('/dev/too', page_development_too),
			# Having this run in prod is an extremely awful idea, until the auth system is implemetned
			('/blog/add_post', blog_add_post), 
		]

		post_routes += [
			# Having this run in prod is an extremely awful idea, until the auth system is implemetned
			('/blog/add_post', add_post_action),
		]
	
	if settings.APRILFOOLS_2024:
		print("April Fools 2024 mode enabled!")

	if settings.APRILFOOLS_2023:
		print("April Fools 2023 mode enabled!")
		get_routes.append(('/why', page_why_af23))

	if settings.APRILFOOLS_2022:
		print("April Fools 2022 mode enabled!")

	if (settings.APRILFOOLS_2024 + settings.APRILFOOLS_2023 + settings.APRILFOOLS_2022) >= 2:
		raise Exception("You can only have one holiday mode enabled at a time. Terminating.")
	
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
		autoescape = jinja2.select_autoescape(default = True)
	)

	app.jinja_env.globals.update({
		'datetime': datetime
	})
	
	return app

class App(web.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

# YanDev code g o

async def page_index(req):
	context = {
		'settings': settings
	}
	return render(req, 'index.aprilfools.2024.html' if settings.APRILFOOLS_2024 else 'index.aprilfools.2023.html' if settings.APRILFOOLS_2023 else 'index.aprilfools.2022.html' if settings.APRILFOOLS_2022 else 'index.updaterollout.html' if settings.ROLLOUT_MODE else 'index.html', context)
	
async def page_projects(req):
	return render(req, 'projects.html', {
		'title': 'Projects'
	})
	
async def page_places(req):
	return render(req, 'places.html', {
		'title': 'Places'
	})

async def page_friendsplaces(req):
	return render(req, 'places.friends.html', {
		'title': 'Friends\' sites | Places'
	})

async def page_miscplaces(req):
	return render(req, 'places.misc.html', {
		'title': 'Misc sites | Places'
	})

async def page_downloads(req):
	return render(req, 'downloads.html', {
		'title': 'Downloads'
	})

async def page_downloads_software(req):
	context = {
		'settings': settings,
		'title': 'Downloads | Software'
	}
	return render(req, 'downloads.software.html', context)

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
	context = {
		'settings': settings,
		'title': 'Downloads | Cursors'
	}
	return render(req, 'downloads.cursors.html', context)

async def page_computers(req):
	return render(req, 'computers.html', {
		'title': 'My computers'
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
		'title': 'Garry\'s Mod | Game servers | HIDNet services',
	})

async def page_gmod_status(req):
	server_info = await get_gmod_server_info()

	return render(req, 'services.gamesrv.gmod.status.html', {
		'title': 'Garry\'s Mod status | Game servers | HIDNet services',
		'server_info': server_info
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
		server_info = await get_mc_server_info(server_ip, server_port)
		server_status = server_info.get('status', False)
		server_name = server_info.get('name', '')
		player_list = server_info.get('players', [])
		icon_b64 = server_info.get('icon', '')
		icon_url = ''
		if icon_b64:
			icon_url = f"data:image/png;base64,{icon_b64}"
		address = server_info.get('address', '')
		# Debugging garbage
		# print(player_list)  
	except:
		server_name = ''
		server_status = False
		player_list = []
		icon_url = ''

	return render(req, 'services.gamesrv.mc.latest.status.html', {
		'title': 'MC server status | Game servers | HIDNet services',
		'server_status': server_status,
		'server_name': server_name,
		'player_list': player_list,
		'icon_url': icon_url,
		'address': address
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

async def page_discord_server_invite(req):
	return render(req, 'discord.invite.html', {
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
	context = {
		'settings': settings,
		'title': 'Compatibility list | Website | Projects'
	}
	return render(req, 'projects.website.compatlist.html', context)

async def page_autos_details(req):
	return render(req, 'projects.autos.html', {
		'title' : 'AutOS | Projects'
	})

async def page_guestbook(req):
	entries = list(reversed(load_entries()))
	banned_ips = load_banned_ips()

	client_ip = req.headers.get('X-Real-IP') or req.headers.get('X-Forwarded-For') or req.remote
	if client_ip in banned_ips:
		return web.Response(text="You are not allowed to view or post to this guestbook as you've been banned. Email hiden64@protonmail.com for more details or to appeal your ban.")

	return render(req, 'guestbook.html', {
		'title': 'Guestbook',
		'entries': entries
	})

async def page_development(req):
	return render(req, 'testing.html', {
		'title': 'Testing | Page 1'
	})

async def page_development_too(req): 
	return render(req, 'testing.too.html', {
		'title': 'Testing | Page 2'
	})

async def page_why_af23(req): 
	return render(req, 'why.aprilfools.2023.html')

async def page_notready(req):
	return render(req, 'nrfs.html', {	
		'title': 'NOT READY YET'
	})
	
async def page_blog(request):
	posts = get_posts()
	context = {
		'posts': posts,
		'title': "Blog"
	}
	return render(request, 'blog.html', context)

async def blog_post(request):
	post_id = request.match_info['post_id']
	posts = get_posts()
	post = get_post_by_id(posts, post_id)
	if not post:
		raise HTTPBadRequest(text='Invalid post ID')
	context = { 
		'post': post,
		'title': post['title']
	}
	return render(request, 'blog.post.html', context)

async def blog_comment(request):
	post_id = request.match_info['post_id']
	posts = get_posts(no_convert=True)
	post = get_post_by_id(posts, post_id)
	if not post:
		raise HTTPBadRequest(text='Invalid post ID')

	form_data = await request.post()
	name = form_data['name']
	email = form_data['email']
	content = form_data['content']
	now = datetime.now().replace(microsecond=0).isoformat()
	comment = {
		"name": name,
		"email": email,
		"content": content,
		"date": now
	}
	post["comments"].append(comment)
	save_posts(posts)

	return web.HTTPFound(f'/blog/post/{post_id}')


async def blog_add_post(request):
	return render(request, 'blog.add_post.html')

async def add_post_action(request: Request):
	form = await request.post()
	title = form.get('title')
	content = form.get('content')
	if not title or not content:
		raise HTTPBadRequest(text='Invalid post format.')

	posts = get_posts(no_convert=True)
	add_post(posts, title, content)
	save_posts(posts)

	return web.HTTPFound('/blog')

async def blog_rss(request):
	posts = get_posts(no_convert=True)
	items = []
	for post in posts:
		item = PyRSS2Gen.RSSItem(
			title=post['title'],
			link=f'{request.scheme}://{request.host}/blog/post/{post["id"]}',
			description=post['content'],
			pubDate=datetime.fromisoformat(post['date'])
		)
		items.append(item)
	rss = PyRSS2Gen.RSS2(
		title="HIDEN's Blog (RSS)",
		link=f'{request.scheme}://{request.host}',
		description="My personal blog.",
		lastBuildDate=datetime.now(),
		items=items
	)
	rssString = rss.to_xml()
	return web.Response(text=rssString, content_type='application/rss+xml')

async def handle_404(req):
	return render(req, '404.html', { 
		'title': 'Page not found' 
		}, status = 404
	)
	
async def get_gmod_server_info():
	address = (settings.GMODHOST, settings.GMODPORT)

	loop = asyncio.get_event_loop()

	try:
		info = await loop.run_in_executor(None, a2s.info, address)
		players = await loop.run_in_executor(None, a2s.players, address)

	except socket.timeout:
		return None

	return {
		'server_name': info.server_name,
		'map_name': info.map_name,
		'num_players': info.player_count,
		'max_players': info.max_players,
		'players': players
	}

async def gb_submission_handler(req):
	data = await req.post()
	name = data['name']
	email = data['email']
	location = data['location']
	website = data['website']
	message = data['message']
	# workaround so that posting works properly
	null = None 

	add_entry(req.remote, null, name, email, location, website, message)

	return web.HTTPFound('/guestbook')

def load_entries():
	if not os.path.exists('json/gb.json'):
		return {}
	with open('json/gb.json', "r") as f:
		data = json.load(f)
		return data

def add_entry(req, ip_address, name, email, location, website, message):
	entries = load_entries()
	banned_ips = load_banned_ips()

	# another workaround so that posting works correctly
	if isinstance(req, aiohttp.web.Request): 
		ip_address = req.headers.get('X-Real-IP') or req.headers.get('X-Forwarded-For') or req.remote

	if ip_address in banned_ips:
		return web.Response(text="You are not allowed to view or post to this guestbook as you've been banned. Email hiden64@protonmail.com for more details or to appeal your ban.")

	new_entry = {
		"name": name,
		"email": email,
		"location": location,
		"website": website,
		"message": message,
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

async def get_mc_server_info(server_ip, server_port):
	async with aiohttp.ClientSession() as session:
		async with session.get(f'https://api.mcsrvstat.us/2/{server_ip}:{server_port}') as resp:
			if resp.status == 200:
				data = await resp.json()
				if data['online']:
					return {
						'status': True,
						'name': data['motd']['clean'][0],
						'players': data['players']['list'] if 'list' in data['players'] else [],
						'icon': data['icon'].replace('data:image/png;base64,', '') if 'icon' in data else '',
						'address': data['hostname'] if 'hostname' in data else ''
					}
				else:
					return {'status': False}
			else:
				return {'status': False}

async def hbot_check_update(req):
	ver = req.query.get('version')
	latest_ver = '1.8.2'
	rel_date = date(2023, 5, 27)

	if ver == latest_ver:
		return web.json_response({'update_available': False})
	elif ver == None or ver > latest_ver:
		raise HTTPBadRequest(text="Invalid version number") 
	else:
		return web.json_response({'update_available': True, 'latest_version': latest_ver, 'release_date': rel_date.isoformat()})

async def hbot_random_cat(request): # switch this to my own host once that's ready
	async with aiohttp.ClientSession() as session:
		response = await session.get('https://cataas.com/cat')
		photo_data = await response.read()
	photo_base64 = 'data:image/jpeg;base64,' + base64.b64encode(photo_data).decode('utf-8')
	return web.json_response({'img_url': photo_base64})

# dumb shit go
def get_posts(no_convert=False):
	with open('json/bp.json', 'r') as f:
		posts = json.load(f)
		for post in posts:
			if not no_convert:
				try:
					post['date'] = datetime.fromisoformat(post['date']).strftime('%B %d, %Y')
				except ValueError:
					pass
			post['content'] = post['content'].replace('<p>', '').replace('</p>', '\n')
			for comment in post['comments']:
				if 'date' in comment:
					try:
						if not no_convert:
							comment['date'] = datetime.fromisoformat(comment['date']).strftime('%B %d, %Y')
					except ValueError:
						pass
		return posts

def save_posts(posts):
	with open('json/bp.json', 'w') as f:
		json.dump(posts, f, ensure_ascii=False, indent=4, default=str)

def get_post_by_id(posts, post_id):
	try:
		post_id_int = int(post_id)
	except ValueError:
		return None
	for post in posts:
		if post['id'] == post_id_int:
			return post
	return None

def add_comment_to_post(post, comment):
	if 'comments' not in post:
		post['comments'] = []
	post['comments'].append(comment)

def add_post(posts, title, content):
	now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
	post_id = len(posts) + 1
	post = {
		'id': post_id,
		'title': title,
		'content': content,
		'date': now,
		'comments': []
	}
	posts.insert(0, post)
	
def render(req, tmpl, context=None, status=200, content_type='text/html'):
	tmpl = req.app.jinja_env.get_template(tmpl)
	content = tmpl.render(context or {}, request=req)
	return web.Response(text=content, content_type=content_type, status=status)