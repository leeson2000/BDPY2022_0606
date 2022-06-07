import collections

from demo10 import courses
from demo8 import course
from pprint import pprint

print("使用list comprehension")
pprint([{'name': c.name, 'attendee': c.attendee} for c in courses])
pprint([{'name': c.name, 'income': c.attendee * 8000} for c in courses])
pprint(tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses))
pprint(tuple({'income': c.attendee * 8000} for c in courses))
