import sqlite3
import time

# 手動建一個db目錄
c1 = sqlite3.connect('db/demo109.sqlite')
QUERY = "SELECT * FROM EMPLOYEE"
cursor = c1.cursor()
allRecords = cursor.execute(QUERY).fetchall()
print(type(allRecords), len(allRecords))
for r in allRecords:
    print(r[0], r[1], r[2], r[3], r[4])
c1.close()