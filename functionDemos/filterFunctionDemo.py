__author__ = 'luowen'

""" construct an iterator from those elements of iterable for which function returns true """

list1 = [1, 2, 3, 4, 5, 6]
def filterFn(x):
    if x > 4:
        return True
    else:
        return False

resultSet = filter(filterFn, list1)
print(list(resultSet))

# lambda version
resultSet = filter(lambda x: x > 4 if True else False, list1)
print(list(resultSet))
