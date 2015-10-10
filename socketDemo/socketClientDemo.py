__author__ = 'Administrator'

"this is a socket client demonstrates"

import socket, glob

s = socket.socket()

s.connect(("127.0.0.1", 50007))  # socketServerDemo must execute first



for file in glob.glob('*.py'):
    with open(file, 'r') as handle:
        for line in handle:
            s.send(line.encode('utf-8'))
while True:
    data = s.recv(100)

    print(list(bytearray(data)))
    print(not data)
s.close()

