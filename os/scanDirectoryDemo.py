__author__ = 'luowen'

"list the directory informations"

import  os

directoryList = os.listdir('./')
print(directoryList)

#directoryList = os.scandir()  # this method is appear in python 3.5 enhance of listdir()
#print(directoryList)
