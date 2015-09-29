__author__ = 'luowen'

"Sqlite3 Demo"

import sqlite3

'''
connector = sqlite3.connect("sqlite3demo.db")  # select database if not exists create it
cursorObj = connector.cursor()  # get cursor object

cursorObj.executescript(
    """
    create table if not exists sqlite3demo_table (id integer, name text, age integer);
    insert into sqlite3demo_table values(1, 'luowen', 23), (2, 'maomao', 21), (3, 'gawin', 23);
    """
)
cursorObj.execute("select * from sqlite3demo_table")
'''

connector = sqlite3.connect('sqlite3demo.db')

for i in connector.execute("select * from {table}".format(table="sqlite3demo_table")):
    print(i)



