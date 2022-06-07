from demo10 import courses
from demo8 import course
from pprint import pprint


def available(c: course):
    return c.attendee >= 8


def isRemote(c: course):
    return c.remote is True


print("8人以上會開課")
pprint(tuple(filter(available, courses)))
print("遠距課程")
pprint(tuple(filter(isRemote, courses)))
print("8人以上會開課,遠距課程")
pprint(tuple(filter(isRemote, filter(available, courses))))
