# Debugging script used while I was fixing a bug regarding the ISO -> Human-readable date conversion in the blog.
# This converts the time from said human-readable format, back to ISO.
# There used to be a bug where vice-versa would happen if someone had posted a comment to a blog post. which has since been fixed.
# This bug is still present with posting to the blog, however. I will look into a fix at a later date.

import json
from datetime import datetime

# Load the existing data
with open('json/bp.json', 'r') as f:
	data = json.load(f)

# Loop over the posts and update the date format
for post in data:
	if 'date' in post:
		old_date = post['date']
		try:  
			new_date = datetime.strptime(old_date, '%B %d, %Y').isoformat()
			post['date'] = new_date
		except ValueError:
			pass

# Save the updated data
with open('json/bp.json', 'w') as f:
	json.dump(data, f)