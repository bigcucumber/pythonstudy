__author__ = 'luowen'
"get random string"

from os import urandom

string = urandom(22)  # get random bytes
print(string)

