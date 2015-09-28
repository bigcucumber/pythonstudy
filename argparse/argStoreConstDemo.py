__author__ = 'Administrator'
"Argument Parser Of Store_Const Demo"
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("constValue", action="store_const", help="default store value", const="ConstDefaultValue")
arguments = parser.parse_args()

print(arguments.constValue)  # default value constDefaultValue
