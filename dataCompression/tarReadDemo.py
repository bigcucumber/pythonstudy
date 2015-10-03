__author__ = 'luowen'

" read tarbag infomation "

import tarfile

tarFileObj = tarfile.open("demo.tar.gz", 'r:gz')  # get file handle

tarInfosObj = tarFileObj.getmembers()

for tarInfoObj in tarInfosObj:
    print("\t {0:<50s} \t {1:<20d} \t {2} \t {3} \t ". format(tarInfoObj.name, tarInfoObj.size, tarInfoObj.type, tarInfoObj.mtime))

tarFileObj.close()  # close file handle
