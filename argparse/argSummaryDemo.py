__author__ = 'Administrator'

"summary demo of python arguments"

import argparse, math

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--numbers', type=int, help="need process numbers", metavar="[0,1,..10]", choices=range(0, 10), required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', help="compute sum of input numbers")
group.add_argument('--avg', help="compute average of input numbers")
group.add_argument('--mid', help="compute median of input numbers")

arguments = parser.parse_args()

resultSet = 0

if arguments.sum:
    resultSet = sum(arguments.sum)
elif arguments.avg:
    resultSet = 11


