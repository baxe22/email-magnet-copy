import sys, re
import link_extractor as le
from collections import deque
import time

try:
	domain = sys.argv[1]
except:
	domain = 'jana.com'

domain_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')
print domain
print not not domain_pattern.match(domain)

starting_url = r'http://'+domain
urls_to_visit = deque()
urls_to_visit.append(starting_url)
visited_urls = set()
while urls_to_visit:
	url = urls_to_visit.popleft()
	if url.startswith('mailto:'):
		print url[7:]
	elif url not in visited_urls:
		visited_urls.add(url)
		child_links = le.extract_links(url)
		valid_children = le.valid_links(child_links, domain)
		for child_link in valid_children:
			if child_link not in visited_urls:
				urls_to_visit.append(child_link)
print 'done'


