__author__ = 'Administrator'

import MySQLdb
"this is MySQLdb library demonatrate reference http://mysql-python.sourceforge.net/MySQLdb.html and https://www.python.org/dev/peps/pep-0249/#connection"

def main():
    connection = MySQLdb.connect('localhost', 'root', 'luowen', 'haha')
    cursorObj = connection.cursor()  # get cursor object

    try:
        cursorObj.execute('select * from pc_wx_fans')
        print(cursorObj.rowcount)  # print the result row count
        fields = tuple(name[0] for name in cursorObj.description)
        resultSet = cursorObj.fetchall()
        arrayList = [dict(zip(fields, result)) for result in resultSet]
        print(arrayList)
    finally:
        connection.close()

if __name__ == '__main__':
    main()
