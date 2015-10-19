__author__ = 'luowen'

import http.client

connection = http.client.HTTPConnection('www.baidu.com', 80)
connection.set_tunnel('www.163.com')
connection.request(method='GET', url='/')

responseObj = connection.getresponse()
while not responseObj.isclosed():
    print(responseObj.read(1024).decode('utf-8'))

