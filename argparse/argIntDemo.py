__author__ = 'Administrator'
"""
covert argument to integer type demo
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int, help="input a number you want to square")
parser.add_argument("-v", "--verbose", help="show detail information", action="store_true")

arguments = parser.parse_args()

resultSet = arguments.square**2
if arguments.verbose:
    print("The square of {0} is {1}".format(arguments.square, resultSet))
else:
    print(resultSet)
exit(0)
