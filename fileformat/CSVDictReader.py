__author__ = 'luowen'

"this is a dictReader for csv"
from csv import DictReader

with open('demo.csv', 'r', encoding='utf-8', newline='') as fileHandle:
    dictReaderObj = DictReader(fileHandle)
    for line in dictReaderObj:
        print(line)

