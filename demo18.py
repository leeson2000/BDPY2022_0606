import collections
from functools import reduce
from demo10 import courses, poop, bdpy, pykt, aiocv, andbiz
from demo8 import course
from pprint import pprint

cplus = course(name="cplus", field="cpp", attendee=20, remote=True)
courses = (poop, bdpy, cplus, pykt, aiocv, andbiz)


def reducer(acc: dict, val: course):
    """
    取得不同field下的課程name列表
    :param acc: 到目前的結果
    :param val: 現在這筆資料
    :return: 加上這筆資料到目前的結果
    """
    # 依照進來的field, 如果是新的field, 就給定一個list
    acc.setdefault(val.field, [])
    acc[val.field].append(val.name)
    return acc


course_by_category = reduce(reducer, courses, {})
pprint(course_by_category)