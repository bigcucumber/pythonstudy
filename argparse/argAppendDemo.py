__author__ = 'Administrator'

" Argument Parser action append Demo"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num", action="append")

arguments = parser.parse_args()

print(arguments.num)

""" as result
python argAppendDemo.py --num 2 --num 3 --num 33
['2', '3', '33']
"""

