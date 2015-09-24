__author__ = 'Administrator'


class Person:
    name = "luowen"
    age = 23

p1 = Person()

print(p1.name)
print(p1.age)

# add a attribute lover for object p1
setattr(p1, "lover", "vv")
print(p1.lover)
