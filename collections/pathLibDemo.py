__author__ = 'luowen'

""" the pathlib is some file and directory operations """
import pathlib, os
from collections import Counter

#  iter current directory
couter = Counter()
path = pathlib.Path('../')
dict1 = dict()
allfile = 0
for i in path.iterdir():
    if not i.is_dir():
        continue
    pyfiles = [j for j in i.glob("*.py")]
    lenfile = len(pyfiles)
    dict1[i.name] = lenfile
    allfile += lenfile

dict1['allfileCnt'] = allfile

for i, j in dict1.items():
    print("director {0} has [{1}] files".format(i, j))



