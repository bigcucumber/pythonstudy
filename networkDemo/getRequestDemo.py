__author__ = 'luowen'
'this is a get demonstrates'

import urllib.request, urllib.parse

postData = urllib.parse.urlencode({"name": "luowen", "age": 23232})

url = "http://localhost/test/demo4py.php?{0}".format(postData)

resultSet = ""
with urllib.request.urlopen(url) as urlHandle:
    for line in urlHandle:
        resultSet += line.decode('utf-8')

print(resultSet)

