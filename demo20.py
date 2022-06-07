import collections
import itertools
from functools import reduce
from demo10 import poop, bdpy, pykt, aiocv, andbiz
from demo8 import course
from pprint import pprint
from itertools import groupby

cplus = course(name="cplus", field="cpp", attendee=20, remote=True)
courses = (poop, andbiz, bdpy, cplus, pykt, aiocv)

courses = sorted(courses, key=lambda x: x.field)
course_by_field = {c[0]: [ele.name for ele in c[1]] for c in itertools.groupby(courses, lambda x: x.field)}
pprint(course_by_field)

print("-" * 180)
for v in itertools.groupby(courses, lambda x: x.field):
    print(type(v[0]), type(v[1]))
    print(v[0])
    print([l.name for l in v[1]])