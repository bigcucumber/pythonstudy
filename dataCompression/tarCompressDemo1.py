__author__ = 'luowen'

" tar bag demo "

import tarfile

tarFileObj = tarfile.open("demo.tar.gz", "w:gz")

tarFileObj.add("./")

tarFileObj.close()

