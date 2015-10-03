__author__ = 'luowen'
"this is a common Writer to create csv file"
import csv

with open('CSVCommonWriter.csv', 'w', encoding="utf-8", newline='') as fileHandle:
    writerObj = csv.writer(fileHandle, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    writerObj.writerow(["luowen"] * 3 + ['v""v'])
    writerObj.writerow(["gawin"] * 3 + ['v,"","",v'])
