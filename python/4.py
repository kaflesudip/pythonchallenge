import urllib3

next_item = 12345
for i in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(str(next_item))
    http_pool = urllib3.connection_from_url(url)
    whole_content = http_pool.urlopen('GET', url).data.decode('utf-8')
    next_item = int(whole_content.split(" ")[-1])
    if next_item == 16044:
        next_item = 16044/2
    print (whole_content, next_item, i)
print (whole_content)

# http://www.pythonchallenge.com/pc/def/peak.html