__author__ = 'Administrator'
"Read all the files in the archive and check their CRC’s and file headers. Return the name of the first bad file, or else return None."

import zipfile
zipFileObj = zipfile.ZipFile('zipArchiveDemo.zip', 'r')
isOk = zipFileObj.testzip()
print(isOk)
