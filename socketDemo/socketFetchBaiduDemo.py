__author__ = 'Administrator'

'this is socket demo to fetch baidu content'

import socket

s = socket.socket()

#s.connect(('127.0.0.1', 50007))
s.connect(('www.baidu.com', 80))

httpHeader = b"GET / HTTP/1.1" \
             b"HOST: www.baidu.com " \
             b"Connection: keep-alive "
s.send(httpHeader)

data = s.recv(1024)
s.close()
print(data)
exit()

while True:
    data = s.recv(1024)
    if data is None: break
    print(data)

s.close()

