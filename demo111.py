import sqlite3
import time

# 手動建一個db目錄
c1 = sqlite3.connect('db/demo109.sqlite')

emp1 = {'Name': "Mark", "Age": 42, "Dept": 1, "Addr": "Taipei"}
emp2 = {'Name': "John", "Age": 43, "Dept": 2, "Addr": "Hsinchu"}
emp3 = {'Name': "Ken", "Age": 44, "Dept": 3, "Addr": "Taipei"}
emp4 = {'Name': "Tim", "Age": 45, "Dept": 4, "Addr": "Hsinchu"}

employees = [emp1, emp2, emp3, emp4]

INSERT_DML = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES(?,?,?,?)"
start_time = time.time()
for emp in employees:
    print((emp['Name'], emp['Age'], emp['Dept'], emp['Addr']))
    c1.execute(INSERT_DML, (emp['Name'], emp['Age'], emp['Dept'], emp['Addr']))

c1.commit()
c1.close()
print("--- %s seconds---" % (time.time() - start_time))
