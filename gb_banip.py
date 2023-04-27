import json

ip = input("Enter an IP address: ")

with open('json/gb_bans.json', 'r') as f:
	banned_ips = json.load(f)
	if ip not in banned_ips:
		banned_ips.append(ip)

with open('json/gb_bans.json', 'w') as f:
	json.dump(banned_ips, f)

print(f"{ip} has been banned from the Guestbook.")