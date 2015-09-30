__author__ = 'Administrator'

" tar compress demo "

import tarfile, os

fileList = []
def printDir(path, level = 1):
    global fileList
    for fileOrDir in os.listdir(path):
        if os.path.isabs(fileOrDir):
            fileOrDir = os.path.basename(fileOrDir)
        if not os.path.isdir(os.path.abspath(fileOrDir)):
            if os.path.isfile(fileOrDir):
                fileList.append(fileOrDir)
        else:
            printDir(os.path.realpath(fileOrDir), level)
    return fileList

currentPath = os.path.realpath('.')
list1 = printDir(currentPath)

filename = 'tarDemo.tar.gz'
tarFileObj = tarfile.TarFile(filename, 'w')

for file in list1:
    tarFileObj.add(file)  # add file to tar bag

tarFileObj.close()

