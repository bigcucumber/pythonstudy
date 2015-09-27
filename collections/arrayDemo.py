__author__ = 'luowen'

""" array demos """

import  array

arr1 = array.array('l', [1, 3, 4, 5])
print(arr1)
print(arr1.typecode)
arr1.append(332323)
print(arr1)
print(arr1.itemsize)

arr1b = array.array('l', [222, 333, 444, 555])
print(arr1b)
arr1.extend(arr1b)
print(arr1)
print("-------")

arr2 = array.array('u', ['a', 'b', 'c', 'd'])
print(arr2)

arr3 = array.array('u', 'abcdef')
print(arr3)
