__author__ = 'luowen'

import hashlib

msg = b'luowen'

hashlibObj = hashlib.md5()
hashlibObj.update(msg)

resultSet = hashlibObj.hexdigest()
print(resultSet)



