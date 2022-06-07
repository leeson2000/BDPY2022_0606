import collections
from functools import reduce
from demo10 import courses
from demo8 import course
from pprint import pprint
import time


def transform(x: course):
    print(f"開始計算%s的利潤" % x.name)
    time.sleep(x.attendee / 3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    return result


start = time.time()
result = tuple(map(transform, courses))
end = time.time()
print("花了%.3f, 結果是:" % (end - start));
pprint(result)