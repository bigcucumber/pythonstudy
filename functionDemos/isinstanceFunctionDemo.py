__author__ = 'luowen'

""" isinstance function return true if the object argument is an instance of the classinfo argument """

string = "abcdef"

instanceType = isinstance(string, str)
print(instanceType)  # print False

instanceType = isinstance(string, int)
print(instanceType)  # print False

instanceType = isinstance(string, set)
print(instanceType)  # print False

string = {'a': 22}
instanceType = isinstance(string, dict)  # print True
print(instanceType)
