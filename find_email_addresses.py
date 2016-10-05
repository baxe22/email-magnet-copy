import sys, re
domain = sys.argv[1]
url_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')
print domain
print not not url_pattern.match(domain)