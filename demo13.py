from demo10 import courses
from demo8 import course
from pprint import pprint

print("全部的內容")
pprint([c for c in courses])
print("會開班的")
pprint([c for c in courses if c.attendee >= 8])
print("有遠距的")
pprint([c for c in courses if c.remote is True])
print("python課")
pprint(tuple([c for c in courses if c.field == "python"]))
print("android課")
pprint(tuple(c for c in courses if c.field == "android"))