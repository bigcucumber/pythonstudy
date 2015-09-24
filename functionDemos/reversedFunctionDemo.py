__author__ = 'luowen'

""" Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0). """


list1 = [1, 2, 3, 4]
print(list1)
list1 = reversed(list1)
print(list(list1))
