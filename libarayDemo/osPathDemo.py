__author__ = 'luowen'

" some os path method "

from os import path
import glob

pathValue = path.curdir
print(pathValue)  # print current path relative path

absPathValue = path.abspath(pathValue)
print(absPathValue)  # print absolute path

dirname = path.dirname(absPathValue)
print(dirname)  # print directory name

print(path.isdir(dirname))  # judgement the dirname is directory result absolute is True
print(path.isfile(dirname))  # judgement the dirname is file result absolute is False

