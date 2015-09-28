#!bin/env python

import argparse

parser = argparse.ArgumentParser()  # create argumentParser Object
parser.add_argument('-v', '--verbose', type=int, choice=[1, 2, 3, 4], help="to show more detail information",
                    action="store_true")  # add arguments

"""
[-v] is the short options
[--verbose] is the whole options
[type=dataType] convert the argument to dataType. default command line argument is string type if you want to covert to integer you can  use type=int. see current directory argIntDemo.py
[choice=listType] when argument is empty or not in listType during the action is not specifying then raise this information on terminal. see the argChoiceDemo.py
[help="your description"] is the description information
[action={"store_true", "count"}] this mean s that if the option is specified, assign the value True to args.verbose. Not specifying it implies False. see argStoreTrueDemo.py and argCountDemo.py

"""

argsOptions = parser.parse_args()

if argsOptions.verbose:
    print('ok')

