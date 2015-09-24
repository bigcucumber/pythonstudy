__author__ = 'luowen'


""" issubclass(classA, classB) judgement classA is subclass of classB """

class ClassB:
    def speak(self):
        print("I am ClassB instance")

class ClassA(ClassB):
    def speak(self):
        print("I an classA instance")

isSubClass = issubclass(ClassA, ClassB)
print(isSubClass)  # print True

isSubClass = issubclass(ClassA, str)
print(isSubClass)  # print False



