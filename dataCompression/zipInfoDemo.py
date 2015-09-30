__author__ = 'Administrator'

"""
    zip information list as follow:
        filename
        compress_type
        compress_size
        date_time
        create_version
        extract_version
        CRC
        file_size
"""

import zipfile

zipFileObj = zipfile.ZipFile('zipArchiveDemo.zip')
zipInfoList = zipFileObj.infolist()

zipInfo = zipInfoList[0]

print(zipInfo.filename)
print(zipInfo.compress_type)
print(zipInfo.compress_size)
print(zipInfo.date_time)
print(zipInfo.create_version)
print(zipInfo.extract_version)
print(zipInfo.CRC)
print(zipInfo.file_size)

