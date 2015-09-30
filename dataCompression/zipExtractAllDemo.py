__author__ = 'Administrator'

" zip bag extract all file Demo "

import zipfile

zipFileObj = zipfile.ZipFile('zipArchiveDemo.zip')

zipFileObj.extractall('./tmp/all')
