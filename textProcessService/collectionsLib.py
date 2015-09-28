__author__ = 'Administrator'

from collections import ChainMap

list1 = [1, 2, 23, 'c']

list2 = ['a', 'b', 'c', 'd']

list3 = ['x', 'y', 'x']

resultSet = ChainMap(list1, list2, list3)

