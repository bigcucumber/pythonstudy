__author__ = "luowen"

""" tuple Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range. """

list1 = [1, 2, 3, 4]

tuple1 = tuple(list1)
print(tuple1)

dict1 = {1: 'a', 2: 'b', 3: 'c'}

tuple2 = tuple(dict1)
print(tuple2)
