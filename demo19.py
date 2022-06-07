import collections
from functools import reduce
from demo10 import poop, bdpy, pykt, aiocv, andbiz
from demo8 import course
from pprint import pprint

cplus = course(name="cplus", field="cpp", attendee=20, remote=True)
courses = (poop, bdpy, cplus, pykt, aiocv, andbiz)


def reducer(acc, val: course):
    """
    取得不同field下的課程name列表
    :param acc: 到目前的結果
    :param val: 現在這筆資料
    :return: 加上這筆資料到目前的結果
    """
    acc[val.field].append(val.name)
    return acc


course_by_category = reduce(reducer, courses, collections.defaultdict(list))
pprint(course_by_category)
print("convert to a normal dict")
pprint(dict(course_by_category))