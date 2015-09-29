__author__ = 'luowen'

"The Data persistence Shelve"

import shelve

data = shelve.open("shelve.bin")

data['integerType'] = 11
data['stringType'] = "gawin"
data['listType'] = [1, 2, 3, 4, 4]
data['dictType'] = {'a': 1, 'b': 2, 'c': 3}
data['setType'] = {'a', 'abc', 'haha'}

data.close()
print("persistence data over")



