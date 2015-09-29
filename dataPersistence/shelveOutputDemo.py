__author__ = 'luowen'

import shelve
" from shelve persistence object fetch data "

with shelve.open('shelve.bin', 'r') as fileHandle:
    for key in fileHandle:
        rint("{0} => {1}".format(key, fileHandle[key]))
