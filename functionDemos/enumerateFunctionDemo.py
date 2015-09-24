__author__ = 'luowen'

# enumerate() return an enumerate object. iterable must be a sequence

string = "abcdef"

enumerate1 = enumerate(string) # return enumerate object

resultSet = list(enumerate1)
print(resultSet)  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]

list1 = [1, 2, 3, 4]
resultSet = list(enumerate(list1))
print(resultSet)  # [(0, 1), (1, 2), (2, 3), (3, 4)]

set1 = {'a', 'y', 'c', 'x'}
resultSet = list(enumerate(set1))
print(resultSet)  # [(0, 'y'), (1, 'a'), (2, 'c'), (3, 'x')] result will change because set type is not sort

