def func1():
    pass


def func2():
    yield


print(type(func1), type(func1()), type(func2), type(func2()))


def func3():
    yield 1
    yield 2
    yield 3


g1 = func3()
print(next(g1), next(g1), next(g1))
# next(g1)

for i in func3():
    print("inside a loop", i)


def func4():
    a = 1
    b = 2
    yield a
    a += b
    yield a


print(next(func4()), next(func4()), next(func4()), next(func4()))
g2 = func4()
print(next(g2), next(g2))