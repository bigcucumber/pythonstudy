__author__ = 'luowen'

'This module provides a portable way of using operating system dependent functionality.'

import os, pathlib, time

osName = os.name  # get system name example  'posix', 'nt', 'ce', 'java'.
print(osName)

termid = os.ctermid()  # get the terminal id available for like-unix
print(termid)

environ = os.environ
#print(environ)  # print the system environment information

#loginUserName = os.getlogin()
#print(loginUserName)

#fileHandle = open('__init__.py')
#encodeName = os.device_encoding(fileHandle)
#print(encodeName)


# create blank file
filename = 'demo_file.py'
modifyNameOfFile = 'demo_file2.py'

pathObj = pathlib.Path(filename)
if not pathObj.is_file():
    with open(filename, 'w') as fileHandle:
        fileHandle.write("haha")

    #time.sleep(3)  # sleep 3 second
    #os.remove('demo_file.py')  # remove demo_file.py file

    # rename a file
    #os.rename(filename, modifyNameOfFile)

# create directory





