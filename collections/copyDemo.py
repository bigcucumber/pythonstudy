__author__ = 'luowen'

"""
Assignment statements in Python do not copy objects, they create bindings between a target and an object
"""

import copy

a = [1, 2, 3, 4, ['a', 'b', 'c']]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

print("{0}, {1}, {2}, {3} is the same now".format(a, b, c, d))

print(a==b==c==d)  # result is true

a.append('appendData')
a[4].append('d')

print(a)
print(b)
print(c)
print(d)  # deepcopy freazont data type


""" result data as below
[1, 2, 3, 4, ['a', 'b', 'c']], [1, 2, 3, 4, ['a', 'b', 'c']], [1, 2, 3, 4, ['a', 'b', 'c']], [1, 2, 3, 4, ['a', 'b', 'c']] is the same now
True
[1, 2, 3, 4, ['a', 'b', 'c', 'd'], 'appendData']
[1, 2, 3, 4, ['a', 'b', 'c', 'd'], 'appendData']
[1, 2, 3, 4, ['a', 'b', 'c', 'd']]
[1, 2, 3, 4, ['a', 'b', 'c']]
"""
