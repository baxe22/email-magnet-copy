import sys, re
import link_extractor as le
from collections import deque

debug = False

try:
	domain = sys.argv[1]
except:
	domain = 'web.mit.edu'
	debug = False

domain_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')
if domain_pattern.match(domain):
	print 'Finding email addresses in '+domain
else:
	print 'Error: Invalid Domain Specified'
	exit()

starting_url = r'http://'+domain
urls_to_visit = deque()
urls_to_visit.append(starting_url)
visited_urls = set()
email_addresses = set()
while urls_to_visit:
	url = urls_to_visit.popleft()
	if debug:
		print url
	if url.startswith('mailto:'):
		email_address = url[7:]
		if email_address not in email_addresses:
			email_addresses.add(email_address)
			print email_address
	elif url not in visited_urls:
		visited_urls.add(url)
		child_links = le.extract_links(url)
		if debug:
			print child_links
		valid_children = le.valid_links(child_links, domain)
		for child_link in valid_children:
			if child_link not in visited_urls:
				urls_to_visit.append(child_link)
print 'Done Searching!'


