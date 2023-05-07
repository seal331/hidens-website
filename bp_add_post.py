from site_ctrl import add_post, get_posts
import json
from datetime import datetime

posts = get_posts()

title = input("Enter the title of the new post: ")
content = input("Enter the content of the new post: ")

add_post(posts, title, content)

with open('json/bp.json', 'w') as f:
	json.dump(posts, f)

print("New post added successfully.")
