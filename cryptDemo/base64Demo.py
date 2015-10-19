__author__ = 'luowen'
'this is a base64 decode and encode demonstrates'

import base64

string = b"this is a base64 decode and encode demonstrates"

encodeString = base64.b64encode(string)
print(encodeString)

decodeString = base64.b64decode(encodeString)
print(decodeString)

