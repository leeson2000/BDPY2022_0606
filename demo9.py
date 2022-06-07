import collections
from pprint import pprint

# define a new namedTuple

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)

courses = [poop, bdpy]
pprint(courses)
del courses[0]
pprint(courses)

courses2 = (poop, bdpy)
pprint(courses2)
# del courses2[0]