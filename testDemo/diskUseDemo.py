__author__ = 'Administrator'

" input a path and get the path usage "

import shutil, argparse, pathlib

parser = argparse.ArgumentParser()

parser.add_argument("path", help="the path you want to calculate")
arguments = parser.parse_args()

pathObj = pathlib.Path(arguments.path)  # get path object
if not pathObj.is_absolute():
    pathObj = pathObj.absolute()

pathString = str(pathObj)  # covert path object to string
diskUse = shutil.disk_usage(pathString)  # get disk usage
i, j, k = diskUse
print("The directory {0} total size: {1}, use size: {2}, free size: {3}".format(pathString, i, j, k))
