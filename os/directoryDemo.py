__author__ = 'luowen'
" operate the path and directory demonstrates "

import pathlib, os


# recursion make directory like shell command `mkdir path -p`
path = './temp/a/b/c/d'
#os.makedirs(path)  # makedirs() compare mkdir()
#os.removedirs(path) #  removedirs() compare rmdir()
#exit()

directoryPathObj = pathlib.Path('temp')

if not directoryPathObj.is_dir():
    os.mkdir(directoryPathObj.name)  # if not exists then create it
else:
    os.removedirs(directoryPathObj.name)  # if exists then delete it
