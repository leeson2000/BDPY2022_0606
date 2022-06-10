import sqlite3

# 手動建一個db目錄
c1 = sqlite3.connect('db/demo109.sqlite')
print("create db successful")
DROP_SQL = "DROP TABLE IF EXISTS EMPLOYEE"
CREATE_SQL = '''
CREATE TABLE EMPLOYEE
(ID INTEGER PRIMARY KEY,
NAME TEXT NOT NULL,
AGE INTEGER NOT NULL,
DEPT INT,
ADDRESS CHAR(50))
'''
c1.execute(DROP_SQL)
c1.execute(CREATE_SQL)

c1.close()