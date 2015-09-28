__author__ = 'Administrator'

"""
    argument parser with choice argument
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int, help="Input a number which you want to compute square.")
parser.add_argument("-v", "--verbose", choices=[1, 2, 3], type=int, help="Show detail information of result")

arguments = parser.parse_args()
resultSet = arguments.square ** 2

if arguments.verbose:
    print("The {0} square result is {1} and the verbose is {2}".format(arguments.square, resultSet, arguments.verbose))
else:
    print(resultSet)


