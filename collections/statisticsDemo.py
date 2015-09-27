__author__ = 'luowen'

""" the statisic demo """

import statistics

list1 = [1, 2, 3, 4, 5, 6]

midNum = statistics.mean(list1)
print(midNum)  # get the average data of list1

medianNum = statistics.median(list1)
print(medianNum)  # get median data of list1

medianNumLow = statistics.median_low(list1)
print(medianNumLow)  # get median lower data of list1

medianNumHigh = statistics.median_high(list1)
print(medianNumHigh)  # get median hight data of list1

medianNumGroup = statistics.median_grouped(list1, 10)
print(medianNumGroup)  # get detail information from https://docs.python.org/3/library/statistics.html

