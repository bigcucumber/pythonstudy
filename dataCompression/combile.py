__author__ = 'luowen'
"compression of bz2 Demo"

import bz2

data = b"abcdefghijk"

# one-shot
compressData = bz2.compress(data)
print(compressData)

decompressData = bz2.decompress(compressData)
print(decompressData)


# BZ2Compressor
bz2Compressor = bz2.BZ2Compressor()
compressData = bz2Compressor.compress(data)
compressData = bz2Compressor.flush()
print(compressData)

# BZ2Decompressor
bz2Decompressor = bz2.BZ2Decompressor()
decompressData = bz2Decompressor.decompress(compressData)
print(decompressData)

# write to file
with bz2.open("bz2Demo.bin", 'wb') as fileHandle:
    fileHandle.write(b"This is a test string %^^&**(())*&$$$")

# read from file
with bz2.open("bz2Demo.bin", 'rb') as fileHandle:
    for line in fileHandle:
        print(line)
__author__ = 'luowen'
"Gzip Demonstrates"

import  gzip, shutil

# compression data

data = b"abcdefghigklmnopqrset"

resultSet = gzip.compress(data)
print(resultSet)

# decompression data
decompresionData = gzip.decompress(resultSet)
print(decompresionData)


# gzip a exists file

with open('__init__.py', 'rb') as fileIn:
    with gzip.open('__init__.py.gz', 'wb') as fileOut:  # different of gzip.open method
        shutil.copyfileobj(fileIn, fileOut)

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




__author__ = 'Administrator'

import zipfile, bz2

with zipfile.ZipFile("zipArchiveDemo.zip", mode="r") as zipFileObj:
    for file in zipFileObj.namelist():
        with zipFileObj.open(file, 'r') as fileInfo:
            content = b"".join(fileInfo)
            deCompressionData = bz2.BZ2Decompressor()
            print(deCompressionData.decompress(content))
__author__ = 'luowen'

"Zlib compression Demo"

import zlib

data = b"abcdefghijklmnopqrst"

resultSet = zlib.crc32(data)
print(resultSet)  # print crc32 value

resultSet = zlib.compress(data, 9)
print(resultSet)  # compression data
depression = zlib.decompress(resultSet)
print(depression)  # decompression data


# compression object demo

compressionObj = zlib.compressobj(4)
resultSet = compressionObj.compress(data)
print(resultSet)  # compression data

decompressionObj = zlib.decompressobj()
resultSet1 = decompressionObj.decompress(resultSet)
print(resultSet1)



__author__ = 'luowen'
