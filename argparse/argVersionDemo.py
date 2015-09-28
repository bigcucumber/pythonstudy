__author__ = 'Administrator'
"argument parser action version Demo"

import argparse

parser = argparse.ArgumentParser(prog="version_demo")
parser.add_argument("--version", action="version", version="%(prog)s 2.0")

arguments = parser.parse_args()

print(arguments)


