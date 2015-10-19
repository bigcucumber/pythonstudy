__author__ = 'luowen'

"this is a post demo"

import urllib.request, urllib.parse

postData = urllib.parse.urlencode({"name": "luowen", "age": 233})

requestObj = urllib.request.Request('http://localhost/test/demo4py.php', postData.encode('utf-8'))
requestObj.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8')

resultSet = ""
with urllib.request.urlopen(requestObj) as urlHandle:
    for line in urlHandle:
        resultSet += line.decode('utf-8')
print(resultSet)

