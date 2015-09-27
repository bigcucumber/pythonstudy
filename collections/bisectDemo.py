__author__ = 'luowen'

'''
This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
'''

from bisect import bisect

def score(score, list1=[60, 70, 80, 90], list2='ABCDF'):
    i = bisect(list1, score())
    return list2[i]
print(scor(33))

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

resultSet = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(resultSet)



