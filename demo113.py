import sqlite3
import time

# 手動建一個db目錄
c1 = sqlite3.connect('db/demo109.sqlite')
QUERY = "DELETE FROM EMPLOYEE"
cursor = c1.cursor()
cursor.execute(QUERY)
c1.commit()
c1.close()
print("delete success")