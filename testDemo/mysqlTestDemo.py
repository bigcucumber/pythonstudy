__author__ = 'Administrator'

import pythonStandardLib.configure.database as database, sqlite3
dbConfig = database.databaseConfig


connector = sqlite3.connect("demo.db")
"""
connector.execute("create table demo (id INTEGER , name text, age INTEGER )")
connector.execute("insert into demo values(1, 'gawin', 23), (2, 'vv', 22)")
connector.commit()
"""
cursorObj = connector.cursor()
cursorObj.execute("insert into demo values(1, 'gawin', 23)")
cursorObj.execute("select * from demo")

connector.close()
