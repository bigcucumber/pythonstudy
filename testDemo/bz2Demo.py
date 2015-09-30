__author__ = 'Administrator'

import bz2

bz2Compressor = bz2.BZ2Compressor()

data = b'hahahah'
bz2Compressor.compress(data)

data2 = b"xixixixix"

bz2Compressor.compress(data2)

compressData = bz2Compressor.flush()
print(compressData)

bz2Decompressor = bz2.BZ2Decompressor()

print(bz2Decompressor.decompress(compressData))

