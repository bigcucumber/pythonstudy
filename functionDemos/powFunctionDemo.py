__author__ = 'luowen'

""" pow function return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z) """


resultSet = pow(2, 3)
print(resultSet)  # print 8

resultSet = pow(2, 3, 2)
print(resultSet)  # print 0 result set is 2**3 % 2 so is 0