__author__ = 'luowen'

import pickle

class JsonDemo:
    name = 'json'
    version = 2.3
    author = 'gawin'

jsonDemo = JsonDemo()
# encoder.encode(jsonDemo) # raise Error json can not serialize customer class object

with open("pickler.bin", mode="wb") as fileHandle:  # serialize jsonDemo object to pickler.bin
    pickle.dump(jsonDemo, fileHandle)

with open("pickler.bin", 'rb') as fileHandle:  # unserialize jsonDemo object from pickler.bin
    resultSet = pickle.load(fileHandle)
    print(resultSet.author)
