__author__ = 'luowen'

"this is common csv reader"

import csv

with open("CSVCommonWriter.csv", 'r', newline="") as fileHandle:
    readerObj = csv.reader(fileHandle)
    for line in readerObj:
        print(line)  # print the csf row data
