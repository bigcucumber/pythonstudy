__author__ = 'Administrator'
'queue demonstrates The Queue is for multi-thread programing.'

import queue, time

queueObj = queue.Queue(2)

isFull = queueObj.full()
print(isFull)

isEmpty = queueObj.empty()
print(isEmpty)

queueObj.put("this is a test A")
queueObj.put("this is a test B")
time.sleep(3)
resultSet = queueObj.get()
print(resultSet)
queueObj.put("this is a test c")



isEmpty = queueObj.empty()
print(isEmpty)

sizeNum = queueObj.qsize()
print(sizeNum)
