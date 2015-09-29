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

