class Person():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person:名字是{self.name}"

    def __repr__(self):
        return f"詳細偵錯==>name:{self.name}"


p1 = Person("Mark")
print("p1 str:", p1)
print(str(p1))
print(repr(p1))

print("傾印p1物件:{}".format(p1))
print("傾印p1物件:{!s}".format(p1))
print("傾印p1物件:{!r}".format(p1))
print("傾印p1物件:{!a}".format(p1))
print("---" * 80)
print("印p1物件:{!s},\n印p1的repr物件{!r},\n印p1的ascii輸出{!a}".format(p1, p1, p1))
print("印p1物件:{0!s},\n印p1的repr物件{0!r},\n印p1的ascii輸出{0!a}".format(p1))