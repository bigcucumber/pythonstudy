__author__ = 'luowen'
'''
Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable
'''
from collections import defaultdict, Counter

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
counter = Counter()

for i, j in s:
    counter[i] += j
print(counter)

d = defaultdict(list)  # defaultdict(type) the type is the dict value type
for k, v in s:
    d[v].append(k)
resultSet = list(d.items())
print(resultSet)
