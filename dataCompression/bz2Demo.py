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
