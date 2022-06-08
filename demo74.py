class Emp:
    pass


class Engineer(Emp):
    pass


class Pm(Emp):
    pass


class Hr(Emp):
    pass


staffs = [(Emp(), "employee1"), (Engineer(), "engineer1"), (Pm(), "pm1"), (Hr(), "hr1")]
classes = [Emp, Engineer, Pm, Hr]

for staff, name in staffs:
    for emp_class in classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print(name, message1, emp_class.__name__)

for class1 in classes:
    for class2 in classes:
        isSubclass = issubclass(class1, class2)
        message = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print(class1.__name__, message, class2.__name__)