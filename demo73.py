class Emp():
    gradeLevel = 6

    def startWork(self):
        pass

    def stopWork(self):
        pass


print(Emp.__dict__)


class RD(Emp):
    pass


print(RD.__dict__)


class PM(Emp):
    pass


print(PM.__dict__)

print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
pm1 = PM()
rd1 = RD()
emp1 = Emp()
print(pm1.gradeLevel, rd1.gradeLevel, emp1.gradeLevel)
RD.gradeLevel = 7
print(RD.__dict__)
print(Emp.__dict__)
print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
print(pm1.gradeLevel, rd1.gradeLevel, emp1.gradeLevel)
Emp.gradeLevel = 5
print(Emp.gradeLevel, RD.gradeLevel, PM.gradeLevel)
print(pm1.gradeLevel, rd1.gradeLevel, emp1.gradeLevel)