__author__ = 'luowen'

""" bytearray is like ord(str) function but return list
If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().
If it is an integer, the array will have that size and will be initialized with null bytes.
If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.
"""

string = "abcx"
resultSet = bytearray(string.encode())
print(list(resultSet))

intValue = 23
resultSet = bytearray(intValue)
print(list(resultSet))

listValue = [1, 3, 4]
resultSet = bytearray(listValue)
print(list(resultSet))

setValue = {1, 3, 9}
resultSet = bytearray(setValue)
print(list(resultSet))

