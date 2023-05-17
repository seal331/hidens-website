# This script converts the blog post format from pre-Pollen Pandemonium to the current format.
# It *will* look ugly. Running it through a beautifier is recommended if you want it to be readable to a reasonable degree.
# It'll likely be removed shortly after the rollout.

import json

with open('json/bp.json', 'r') as f:
	data = json.load(f)

posts = []

for date, content_list in data.items():
	content = '\n'.join(content_list)
	
	post = {
		'id': len(posts) + 1,
		'title': '',
		'content': content,
		'date': date,
		'comments': []
	}
	posts.append(post)

with open('bp-new.json', 'w') as f:
	json.dump(posts, f)
	print("Done. Rename bp-new.json to bp.json.")
	print("NOTE: The file will look ugly. Please run it through a beautifier if you want it to be readable to a non-masochistic level.")