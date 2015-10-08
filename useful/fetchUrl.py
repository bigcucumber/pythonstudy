__author__ = 'luowen'
"this is multiple thread Demo"
from collections import deque
import threading, random, time

class FetchUrl(threading.Thread):
    """ define the fetch url class """

    dequeValue = 0
    def run(self):
        randomValue = random.randint(0, 6)
        time.sleep(randomValue)
        self.dequeValue = self.dequeValue + 1
        print("thie thread name is : {0} and dequeValue is : {1}".format(self.getName(), self.dequeValue))
