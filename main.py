import urllib2
import html2text
import re
from time import sleep
from bs4 import BeautifulSoup, SoupStrainer



#################################################################
x = 15


url='https://www.reddit.com/r/mrlinks6000/.json'

sleep(10)
page = urllib2.urlopen(url)
sleep(10)

html_content = page.read()
sleep(10)

rendered_content = html2text.html2text(html_content)
sleep(10)
	

file = open('file_text.txt', 'w')

file.write(rendered_content)


with open('file_text.txt','r') as f:
    for link in BeautifulSoup(f.read(), "lxml", parse_only=SoupStrainer('a')): 
        if link.has_attr('href'):
			f1=open('links.txt', 'w+')
			print(link['href'])
			f1.write(link['href'])
			
f1.close()




######################################################