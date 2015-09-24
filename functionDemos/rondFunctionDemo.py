__author__ = 'luowen'


""" Return the floating point value number rounded to ndigits digits after the decimal point. """

randomValue = round(1000.222, 1)
print(randomValue)  # print 1000.2

print("{0:0.1f}".format(1000.222))  # the same form round
