__author__ = 'luowen'

"The linecache module allows one to get any line from a Python source file"
import linecache

content = linecache.getline("./osPathDemo.py", 1)
print(content)  # get the first line