__author__ = 'luowen'

"this is configure demo"

import configparser

configObj = configparser.ConfigParser()

configObj['default'] = {
    "name": 'luwoen',
    "age": 23,
    "lover": "maomao"
}

configObj['gawin'] = {}
configObj['gawin']['domain'] = 'www.gawin.com'
configObj['gawin']['port'] = '80'
configObj['gawin']['username'] = 'gawin'
configObj['gawin']['password'] = 'luowen'

with open('config.ini', 'w', encoding= 'utf-8') as fileHandle:
    configObj.write(fileHandle)
