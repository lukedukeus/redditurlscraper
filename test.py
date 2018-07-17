import re
string = open('log.txt').read()
new_str = re.sub('[^a-z:/?=+@!#$%^&*A-Z0-9\n\.]', ' ', string)
open('log.txt', 'w').write(new_str)