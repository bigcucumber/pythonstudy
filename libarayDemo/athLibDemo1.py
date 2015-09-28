__author__ = 'luowen'

" some adverse features of pathlib"

import pathlib, glob

currentPath = pathlib.Path('.')  # get current path
absCurrentPath = currentPath.absolute()  # get current absolute path

isDir = absCurrentPath.is_dir()  # judge the path is directory
isFile = absCurrentPath.is_fifo()  # judge the path is file
isInfo = absCurrentPath.is_fifo()  # judge the path is fifo
isSymLink = absCurrentPath.is_symlink()  # judge the path is system link
isDeviceBlock = absCurrentPath.is_block_device()  # judge the path is device block
isCharDevice = absCurrentPath.is_char_device()  # judge the path is char device
isSocket = absCurrentPath.is_socket()  # judge the path is socket file


pathValue1 = pathlib.Path("/home")
pathValue2 = pathlib.Path('luowen')
combilePath = pathValue1.joinpath(pathValue2)
print(combilePath)

pathValue1 = pathlib.Path('.')
combilePath = pathValue1 / "../collections"
absolutePath = combilePath.resolve()

for i in absolutePath.iterdir():
    print(i)

windowPath = pathlib.PureWindowsPath("c:/", 'windows', 'system32')
print(windowPath)

print(windowPath.root)
parents = windowPath.parents

for parent in parents:
    print(parent)
