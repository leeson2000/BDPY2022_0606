import collections
from functools import reduce
from demo10 import courses
from demo8 import course
from pprint import pprint
import time
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os


def transform(x: course):
    print(f"[{os.getpid()}]開始計算%s的利潤" % x.name)
    time.sleep(x.attendee / 3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"[{os.getpid()}]計算%s的利潤結束了" % x.name)
    return result


if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor() as p1:
        result = tuple(p1.map(transform, courses))
    end = time.time()
    print("花了%.3f, 結果是:" % (end - start))
    pprint(result)
