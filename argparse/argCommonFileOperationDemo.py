__author__ = 'luowen'

import argparse, sys, re

parser = argparse.ArgumentParser()

parser.add_argument("input", type=argparse.FileType("r"), default=sys.stdin, nargs="?")
parser.add_argument("output", type=argparse.FileType("w"), default=sys.stdout, nargs="?")

arguments = parser.parse_args()
output = arguments.output

for i in arguments.input:
    command = i.strip().lower()
    if re.findall('exit|quit', i):
        print('customer quit.')
        exit(0)
    output.write(i)
