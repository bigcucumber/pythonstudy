__author__ = 'Administrator'

"argument parse action store_false demo"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--defaultValue", action="store_false")

arguments = parser.parse_args()

print(arguments.defaultValue)

""" as result
python argStoreFalseDemo.py --defaultValue
False
"""
