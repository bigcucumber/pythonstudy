__author__ = 'luowen'

import io

BytesIO = io.BytesIO(b'hahahaxixihehe')

print(BytesIO.writable())
print(BytesIO.readable())
print(BytesIO.tell())

resultSet = BytesIO.getvalue()

print(resultSet)
BytesIO.close()
