__author__ = 'luowen'

""" str function is covert other data type to string type """

numValue = 2322233
list1 = [1, 3, 3, 4]

strValue = str(numValue)
print(strValue)  # 232233
print(type(strValue))  # <class 'str'>

strValue1 = str(list1)
print(strValue1)
print(type(strValue1))  # <class 'str'>



""" repr function is print for machine  """

numValue = 2322233
list1 = [1, 3, 3, 4]
reprValue = repr(numValue)
print(reprValue)
print(type(reprValue))

reprValue1 = repr(list1)
print(reprValue1)
print(type(reprValue1))
