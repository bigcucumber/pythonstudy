__author__ = 'Administrator'
"argument parser action='count'"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="count", help="action='count' demo")
arguments = parser.parse_args()

if arguments.verbose and arguments.verbose >= 2:  # when -vv or -vv... execute here
    print('-v argument more than two')
else:
    print('-v is not specifying or less than one')  # when not specify -v or -v execute here


