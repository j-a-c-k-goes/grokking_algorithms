#!/usr/bin/python3.11
"""
    @name simplecaching.py
    @purpose Demonstrate using a hash table to cache data.
"""
# Using a hash table to check if a voter has already voted.
voted = { "tom": "tom" }
def check_voter(name):
	if voted.get(name):
		print(f"{name} has already voted!")
	else:
		voted[ name ] = True
		print(f"{name} is eligible to vote.")

# Using a hash table to cache some data.
cache = {}
def get_page(url):
	if cache.get(url):
		print("Data is in cache.")
		return cache[url]
	else:
		print("Data is not in cache. Checking server for this data.")
		data = get_data_from_server(url)
		cache[url] = data
		return data

def get_data_from_server(url_value):
	server = { "url": "https://testcache.com" }
	if server.get("url"):
		print("Found url data on server.")
		if server["url"] == url_value:
			data_to_return = server["url"]
			return data_to_return
		else:
			print("No url with this name on server.")
	else:
		print("Server contains no data like this.")
		return 1
