#!bin/env python
"""
[-v] is the short options
[--verbose] is the whole options
[type=dataType] convert the argument to dataType. default command line argument is string type if you want to covert to
    integer you can  use type=int. see current directory argIntDemo.py
[choice=listType] when argument is empty or not in listType during the action is not specifying then raise this
    information on terminal. see the argChoiceDemo.py
[help="your description"] is the description information
[action={"store", "store_true", "store_false", "store_const", "version", "count"}] this mean s that if the option is
    specified, assign the value
    True to args.verbose. Not specifying it implies False. see
        argStoreTrueDemo.py
        argStoreFalseDemo.py
        argStoreConstDemo.py
        argCountDemo.py
        argAppendDemo.py
        argVersionDemo.py
[metavar] good show for help information see argMetavarDemo.py
[require={true, false}] the argument is necessary or not for example parser.add_argument("--input", require=true)
    the --input argument must specifying
[dest] allow customer attribute name to be provided see argDestDemo.py
"""
import argparse

parser = argparse.ArgumentParser()  # create argumentParser Object
parser.add_argument('-v', '--verbose', type=int, choice=[1, 2, 3, 4], help="to show more detail information",
                    action="store_true")  # add arguments
argsOptions = parser.parse_args()

if argsOptions.verbose:
    print('ok')

