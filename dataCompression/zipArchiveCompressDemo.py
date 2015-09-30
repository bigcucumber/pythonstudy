__author__ = 'Administrator'

from os import path
from bz2 import BZ2Compressor
import zipfile, glob

" zip archive demo "

currentPath = path.abspath('.')
files = glob.glob1(currentPath, "*.py")  # get current path all python file

zipFileObj = zipfile.ZipFile('zipArchiveDemo.zip', mode="w")  # create a zipFile object

for file in files:
    bz2Compressor = BZ2Compressor()  # create compressor object
    with open(file, 'r') as fileStream:
        content = "".join(fileStream).encode()  # compressive data
    bz2Compressor.compress(content)
    zipFileObj.writestr(file + ".bz2", bz2Compressor.flush())  # put to file
zipFileObj.close()  # close stream




