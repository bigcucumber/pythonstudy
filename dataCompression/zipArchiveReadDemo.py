__author__ = 'Administrator'

import zipfile, bz2

fhandle = open('combile.py', 'wb')
with zipfile.ZipFile("zipArchiveDemo.zip", mode="r") as zipFileObj:
    for file in zipFileObj.namelist():
        with zipFileObj.open(file, 'r') as fileInfo:
            content = b"".join(fileInfo)
            deCompressionData = bz2.BZ2Decompressor().decompress(content)  # decompression data
            fhandle.write(deCompressionData)  # get the content of zip file write to combile.py
fhandle.close()
