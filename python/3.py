import urllib3
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
http_pool = urllib3.connection_from_url(url)
whole_content = http_pool.urlopen('GET', url).data.decode('utf-8')
required_string = ''.join(re.findall('<!--.*-->', whole_content, re.S))
output = ''.join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', required_string))
print (output)

# http://www.pythonchallenge.com/pc/def/linkedlist.php