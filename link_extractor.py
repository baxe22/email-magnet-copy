import requests, urlparse
from lxml import html

def extract_links(url):
	try:
		page = requests.get(url)
		tree = html.fromstring(page.content)
		links = tree.xpath('//a/@href')
		formatted_links = [urlparse.urlparse(link, 'http').geturl() for link in links]
		return formatted_links
	except:
		return []

def valid_links(links, domain):
	return [link for link in links if is_valid_link(link, domain)]

def is_valid_link(link, domain):
	if 'www.'+domain in link or link.startswith('mailto:'):
		return True
	elif '.'+domain in link:
		return False
	else:
		return domain in link