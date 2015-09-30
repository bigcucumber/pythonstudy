__author__ = 'Administrator'

" zip bag extract demo"

import zipfile

zipFileObj = zipfile.ZipFile('zipArchiveDemo.zip', 'r')

name = 'bz2Demo.py.bz2'
zipFileObj.extract(name, "tmp")  # extract bz2Demo.py.bz2 to current tmp directory
