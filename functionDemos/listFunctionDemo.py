__author__ = 'Administrator'

# zip is aggregation function
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
print(list(zip(list1, list2)))
print(set(zip(list1, list2)))
print(dict(zip(list1, list2)))
