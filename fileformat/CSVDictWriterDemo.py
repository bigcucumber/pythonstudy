__author__ = 'luowen'
"this is a csv dict writer"
import csv

with open("demo.csv", 'w', encoding='utf-8', newline="") as fileHandle:
    dictWriterObj = csv.DictWriter(fileHandle, fieldnames=['firstName', 'lastName'])
    dictWriterObj.writeheader()
    dictWriterObj.writerows([{'firstName': 'luo', 'lastName': 'wen'}, {'firstName': 'mao', 'lastName': 'wei'}])
    #dictWriterObj.writerow({'firstName': 'luo', 'lastName': 'wen'})
