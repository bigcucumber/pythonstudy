__author__ = 'Administrator'
" argument parse metavar"

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sort", metavar="desc", default="desc")
parser.add_argument("files", metavar="*.py", default="*.py")

arguments = parser.parse_args()
print(arguments)

"""
python argMetavarDemo.py *.txt
Namespace(files='*.txt', sort='desc')
"""


