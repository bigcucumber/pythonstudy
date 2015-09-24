__author__ = 'luowen'

# id(object) return a integer value  which is guaranteed to be unique and constant for this object during its lifetime
string = "abcd"
idValue = id(string)
print(idValue)

string2 = "abcd"
id2Value = id(string2)
print(id2Value)

idValue = id2Value  # result is true
