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



