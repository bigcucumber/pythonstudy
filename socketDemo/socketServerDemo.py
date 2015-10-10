__author__ = 'Administrator'
"this is a server socket"

import socket

ss = socket.socket()

ss.bind(("", 50007))
ss.listen(2)
while True:
    s, addr = ss.accept()

    print("Host IP: {0} Connected.".format(addr))

    while True:
        data = s.recv(1024)
        if not data:
            break
        s.send(data)
        print(data)

    s.close()

