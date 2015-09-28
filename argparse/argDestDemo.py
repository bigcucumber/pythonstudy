__author__ = 'Administrator'
"argument parser dest"

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--files', dest="ff")

arguments = parser.parse_args()
print(arguments)

""" as result mv default attribute files to ff
Namespace(ff=None)
"""