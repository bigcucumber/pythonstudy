__author__ = 'luowen'

import urllib.parse

parserObj = urllib.parse.urlparse(url="www.baidu.com", scheme="https")
print(parserObj)

postData = urllib.parse.urlencode({"name": "luowen", "age":23})
print(postData)  # print name=luowen&age=23 like http_build_query in php

splitResultObj = urllib.parse.urlsplit("http://www.google.com.hk/s/secen.jpg?from=python")
print(splitResultObj)

urllib.parse.url

