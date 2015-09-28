__author__ = 'Administrator'
"argument parser options action='store_true'"

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true", help="store_ture demo")
arguments = parser.parse_args()

if arguments.verbose:
    print("argument specifying -v or --verbose")
else:
    print("argument not specifying -v or --verbose")
