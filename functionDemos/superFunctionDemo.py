__author__ = 'luowen'


""" super function return a proxy object that delegates method calls to a parent or sibling class of type """

class Human:
    def say(self):
        print("hello human")

class Male(Human):
    def say(self):
        super().say()
        print("hello Male")

male = Male()

male.say()  # print hello human \n hello Male
