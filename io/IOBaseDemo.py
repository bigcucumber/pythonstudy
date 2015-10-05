__author__ = 'luowen'

import io

IOBaseObj = io.IOBase('__init__.py', 'w')

isatty = IOBaseObj.isatty()
print(isatty)

iswritable = IOBaseObj.writable()
print(iswritable)

isreadable = IOBaseObj.readable()
print(isreadable)

