__author__ = 'luowen'
"this is a thread Demo"

from pythonstudy.useful import fetchUrl
import threading, random
threadDemo = threading.Thread()

threadDemo.start()

threadName = threadDemo.name
print(threadName)

isAlive = threadDemo.is_alive()
print(isAlive)

currentThread = threading.current_thread()
print(currentThread.name)

for index in range(1, 10):
    threadDemo = fetchUrl.FetchUrl()
    threadDemo.start()

