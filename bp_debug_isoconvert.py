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