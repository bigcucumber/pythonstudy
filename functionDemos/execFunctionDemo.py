__author__ = 'luowen'

""" This function supports dynamic execution of Python code
    different for eval() function eval() function just execute a python expression
    and can not execute python sentence
"""

i = 10
code = "if i > 3: print('{0} is max than 3'.format(i))"
exec(code)

class ExecDemo:
    """this is a test object"""
    def sayHello(self):
        print("Hello World.")

code = "i = ExecDemo(); i.sayHello()"

exec(code)
