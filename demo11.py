from demo10 import courses
from pprint import pprint


def xyz(x):
    """
    a filter function, to filter remote course
    :param x:
    :return:
    """
    return x.remote is True


result1 = tuple(filter(xyz, courses))
pprint(result1)

# 小於10人
result2 = tuple(filter(lambda course: course.attendee < 10, courses))
pprint(result2)

f1 = filter(lambda c: c.field == "python", courses)
print(type(f1))
print(dir(f1))
for f in f1:
    print(f)
print("---show next---")
f2 = filter(lambda c:c.field == "android", courses)
print(next(f2))