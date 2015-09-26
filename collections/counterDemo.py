__author__ = 'luowen'

"""
A counter tool is provided to support convenient and rapid tallies
"""

from collections import Counter

counter = Counter()

list1 = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 1]

for i in list1:
    counter[i] += 1

print(counter)
print(list(counter.elements())) # print the element of list1
print(counter.most_common(2))  # print [('b', 2), ('a', 2)]


# counter subtract method
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)  # print Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6} actually c - d



