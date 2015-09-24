__author__ = 'luowen'


""" bytes function return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256 """

string = "abcd"

bytesValue = bytes(string.encode())
print(list(bytesValue))

# use bytearray function

bytesValue = bytearray(string.encode())
print(list(bytesValue))

