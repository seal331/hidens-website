# Revereses the ID list for the blog posts.
# Meant to be used in tandem with bp_migration, since that has a quirk where the ID list is reversed from how it should be.

import json

with open('json/bp.json', 'r') as f:
	posts = json.load(f)

# Reverse the order of the ids
for i in range(len(posts)):
	posts[i]['id'] = len(posts) - i

with open('json/bp_reversed.json', 'w') as f:
	json.dump(posts, f, indent=4)
