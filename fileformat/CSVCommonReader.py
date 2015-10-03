__author__ = 'luowen'

"this is a common reader to reader csv file"

import  csv

with open('CSVCommonWriter.csv', 'r', newline='') as fileHandle:
    commonReader = csv.reader(fileHandle, delimiter=',')
    for line in commonReader:
        print(line)  # print line convert to list
        #print(type(line))
