__author__ = 'luowen'

""" judgement a object is callable """

obj = 'abc'

print(callable(obj))  # print False

def fn():
    print("is function")

print(callable(fn))  # print True
