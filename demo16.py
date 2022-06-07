import collections
from functools import reduce
from demo10 import courses
from demo8 import course
from pprint import pprint

total_income = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
pprint(total_income)
total_revenue = reduce(lambda acc, value: acc + value['income'], total_income, 0)
print("total revenue=%d" % total_revenue)
print("total revenue using sum:%d" % sum(x['income'] for x in total_income))
