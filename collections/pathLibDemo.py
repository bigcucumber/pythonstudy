__author__ = 'luowen'

""" the pathlib is some file and directory operations """
import pathlib, os

osName = os.name.lower()

purePath = pathlib.PurePath('/home/luowen')
purePath1 = pathlib.PureWindowsPath('c:/windowns')
print(purePath1)
print(purePath)


