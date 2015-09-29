__author__ = 'luowen'
" Json Demo "
import json

data = [1, 3, 45, 23, {'a': 2323, 'b': 22, 'c': 23}, 'a']
encoder = json.JSONEncoder()
resultSet = encoder.encode(data)
print(resultSet)  # encode complex data
decoder = json.JSONDecoder()
resultSet = decoder.decode(resultSet)
print(resultSet)  # decode json data to complex data
# json.dump(encoder.encode(data), dataHandle) # serialize json data to picker.bin


# serialize to jsonDemo.bin
data = [1, 3, 45, 23, {'a': 2323, 'b': 22, 'c': 23}, 'a']
resultSet = encoder.encode(data)

with open('jsonDemo.bin', 'w') as fileHandle:
    json.dump(resultSet, fileHandle)  # serialized data to jsonDemo.bin

with open('jsonDemo.bin', 'r') as fileHandle:
    resultSet = json.load(fileHandle)
    print("unserialized data from jsonDemo.bin {0}".format(resultSet))
