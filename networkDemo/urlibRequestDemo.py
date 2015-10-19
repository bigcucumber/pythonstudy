__author__ = 'luowen'

import urllib.request, urllib.parse

with urllib.request.urlopen("http://www.baidu.com") as urlHandle:
    #for line in urlHandle:
        #print(line.decode('utf-8'))
    data = urlHandle.read(200)
    print(data)

requestObj = urllib.request.Request('http://www.baidu.com/s/share/qq.html', {'a': 'luowen', 'b': 'maomao'})
print(requestObj.full_url)  # print the full url
print(requestObj.type)  # print schema of url
print(requestObj.host)  # print host
print(requestObj.origin_req_host)  # print origin host
print(requestObj.headers)  # print request headers
print(requestObj.selector)  # get path of url
print(type(requestObj.data))  # print url data

requestObj.add_header("Host", "www.baidu.com")
requestObj.add_header("Connecton", "keep-alive")
print(requestObj.header_items())

