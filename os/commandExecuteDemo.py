__author__ = 'luowen'

import os

command = "ps aux | grep py"

resultSet = os.system(command)
