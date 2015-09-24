__author__ = 'luowen'

"""
Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument.
Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0).
If it does not support either of those protocols, TypeError is raised.
If the second argument, sentinel, is given, then object must be a callable object.
The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.
"""
list1 = enumerate("abcde")
resultSet = iter(list1)
print(list(resultSet))
