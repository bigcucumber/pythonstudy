__author__ = 'Administrator'

"""
    archive bag operation
    implement tar compression
"""

from pathlib import Path
from tempfile import TemporaryFile
import shutil, argparse


parser = argparse.ArgumentParser()
types = dict(shutil.get_archive_formats())  # get support type of system

parser.add_argument("targz", help="input a targz name")
parser.add_argument("input", help="directory need to compression")
parser.add_argument("output", help="compression file output directory")
parser.add_argument("--type", help="type of compression", choices=types, default="tar")

arguments = parser.parse_args()

pathObj = Path(arguments.input)

if not pathObj.is_absolute():
    pathObj = pathObj.absolute()

pathString = str(pathObj)

destFilePath = shutil.make_archive(base_name=TemporaryFile().name, format=arguments.type, root_dir=arguments.input)

shutil.copyfile(destFilePath, arguments.output)
print(destFilePath)

