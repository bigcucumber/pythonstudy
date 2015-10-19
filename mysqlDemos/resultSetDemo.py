__author__ = 'Administrator'

"get result as dict type"

import MySQLdb, configparser

def main():
    sql = 'select id, corp_id from pc_wx_fans'
    resutltSet = fetchOne(sql)
    print(resutltSet)


def getConfig():
    'get mysql dataase config file'
    configObj = configparser.ConfigParser()
    configObj.read('db.ini')
    return dict(configObj.items('MYSQL'))

def query(sql):
    dbConfig = getConfig()
    connection = MySQLdb.connect(dbConfig['host'], dbConfig['user'], dbConfig['password'], dbConfig['database'], int(dbConfig['port']))
    try:
        cursorObj = connection.cursor()
        cursorObj.execute(sql)
        return cursorObj
    finally:
        connection.close()

def fetchOne(sql):
    cursorObj = query(sql)
    return cursorObj.fetchone()

def fetchAll(sql):
    cursorObj = query(sql)
    return cursorObj.fetchall()

if __name__ == '__main__':
    main()
