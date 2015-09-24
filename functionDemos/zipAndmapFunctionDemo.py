__author__ = 'luowen'

""" zip function make an iterator that aggregates elements from each of the iterables.  """

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipObj = zip(list1, list2)
list1 = list(zipObj)
print(list1)

dict1 = dict(list1)
print(dict1)


""" map function return an iterator that applies function to every item of iterable, yielding the results. """

list1 = [1, 2, 3]
map1 = map(lambda x: x*x, list1)
print(list(map1))

