__author__ = 'Administrator'

"summary demo of python arguments"

import argparse, statistics

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--numbers', type=int, nargs='*', help="need process numbers", metavar="[0,1,..10]", choices=range(0, 10), required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument('--sum', help="compute sum of input numbers", action="store_true")
group.add_argument('--avg', help="compute average of input numbers", action="store_true")
group.add_argument('--mid', help="compute median of input numbers", action="store_true")

arguments = parser.parse_args()

resultSet = 0

if arguments.avg:
    resultSet = statistics.mean(arguments.numbers)  # if specifying the --avg then calculate the average data
elif arguments.mid:
    resultSet = statistics.median(arguments.numbers)  # if specifying the --mid then calculate the median data
else:
    resultSet = sum(arguments.numbers)  # default calculate summary data
print(resultSet)
