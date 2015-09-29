__author__ = 'Administrator'

" like like unix command "

import shutil


resultSet = shutil.which('python')
print(resultSet)
resultSet = shutil.which('ls')
print(resultSet)

resultSet = shutil.which('cat')
print(resultSet)
