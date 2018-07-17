import urllib2
from time import sleep



with open('log.txt', 'r') as f:
    urls = []
    for url in f:
		  opener = urllib2.build_opener()
		  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		  response = opener.open(url)
		  sleep(.2)
		  
