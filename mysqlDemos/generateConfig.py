__author__ = 'Administrator'
'gengerate mysql db configure file'

import configparser

def main():
    configObj = configparser.ConfigParser()
    configObj.add_section('MYSQL')
    configObj.set('MYSQL', 'host', 'localhost')
    configObj.set('MYSQL', 'user', 'root')
    configObj.set('MYSQL', 'password', 'luowen')
    configObj.set('MYSQL', 'database', 'haha')
    configObj.set('MYSQL', 'port', '3306')
    configObj.set('MYSQL', 'charater', 'utf-8')

    with open('db.ini', 'w') as fileHandle:
        configObj.write(fileHandle)

if __name__ == '__main__':
    main()
