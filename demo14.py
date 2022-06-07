import collections

from demo10 import courses
from demo8 import course
from pprint import pprint

name_and_field = map(lambda x: {'name': x.name, 'field': x.field}, courses)
pprint(tuple(name_and_field))

description = collections.namedtuple('description', ['name', 'field'])
nameAndFieldTuple = map(lambda x: description(name=x.name, field=x.field), courses)
pprint(tuple(nameAndFieldTuple))
