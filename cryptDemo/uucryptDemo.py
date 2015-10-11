__author__ = 'luowen'
"uu module allowing arbitrary binary data to be transferred over ASCII-only connections"

import uu

# encode demo
inFile = open('base64Demo.py', 'rb')
outFile = open('tmp.bin', 'wb')
uu.encode(inFile, outFile)

# decode demo
inFile = open('tmp.bin', 'rb')
outFile = open('base64demo1.py', 'wb')
uu.decode(inFile, outFile)
