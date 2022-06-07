import collections
from functools import reduce
from demo10 import courses
from demo8 import course
from pprint import pprint

courseByCategory = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}}, courses,
                          {'python': [], 'android': []})
print(courseByCategory)

d1 = {'a': ['Apple'], 'b': ['Banana']}
d2 = {'c': ['Cooke'], 'd': ["donut"]}
print({**d1, **d2})
print({'a': ['Apple'], 'b': ['Banana'], 'c': ['Cooke'], 'd': ["donut"]})
