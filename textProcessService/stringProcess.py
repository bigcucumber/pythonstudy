__author__ = 'Administrator'

# format function
string = "luowen-{0}"
resultSet = str.format(string, "Yes .")
print(resultSet)
resultSet = string.format("Year .")
print(resultSet)


# [Format Specification Mini-Language] you can get mor detail from https://docs.python.org/3/library/string.html#string-constants
"""
format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

# examples
resultSet = '{0}, {1}, {2}'.format('a', 'b', 'c')
print(resultSet)  # print a, b, c

resultSet = '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
print(resultSet)  # print a, b, c

resultSet = '{2}, {1}, {0}'.format('a', 'b', 'c')
print(resultSet)  # print c, b, a

resultSet = '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
print(resultSet)  # print c, b, a

resultSet = '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
print(resultSet)  # print abracababra

resultSet = 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
print(resultSet)  # print Coordinates: 37.24N, -115.81W

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
resultSet = 'Coordinates: {latitude}, {longitude}'.format(**coord)
print(resultSet)  # print Coordinates: 37.24N, -115.81W

coord = (3, 5)
resultSet = 'X: {0[0]};  Y: {0[1]}'.format(coord)
print(resultSet)  # print X: 3;  Y: 5


# Replacing %s and %r:
resultSet = "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
print(resultSet)

# aligning text and specifying string width
resultSet = '{:<30}'.format('left aligned')
print(resultSet)  # string width is 30 and align left

resultSet = '{:>30}'.format('right aligned')
print(resultSet)  # string width is 30 and align right

resultSet = '{:^30}'.format('centered')
print(resultSet)  # string width is 30 and align center

resultSet = '{:*^30}'.format('centered')  # use '*' as a fill char
print(resultSet)  # string width 30 and algin center and fill space with '*' left aligned so the result is '***********centered***********'


# help function demo

# split a string to list
stringValue = "abcd"
resultSet = stringValue.split("c")
print(resultSet)

# split all to list anther method
resultSet = [i for i in stringValue]
print(resultSet)

# capitalize method
print(stringValue.capitalize())

# join method
resultSet = str.join(stringValue.capitalize(), 'xyz'.upper())
print(resultSet)  # print XAbcdYAbcdZ


