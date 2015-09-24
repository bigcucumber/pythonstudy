__author__ = 'luowen'

""" get a attribute from object """
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("luowen")

attr1 = getattr(p1, 'name')
print(attr1)


setattr(p1, 'age', 33)
attr2 = getattr(p1, 'age')
print(attr2)

delattr(p1, 'name')

if hasattr(p1, 'name'):
    attr3 = getattr(p1, 'name')
    print(attr3)
else:
    print("p1 has no attribute of name")
