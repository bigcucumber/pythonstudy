__author__ = 'Administrator'
" when two argument has conflict can use `add_mutually_exclusive_group` method "

import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument("-q", "--quiet", action="store_true", help="quiet execute")
group.add_argument("-v", "--verbose", action="store_true", help="verbose execute")

parser.add_argument("controller", help="the controller need to execute")
arguments = parser.parse_args()

print("executed ok")

