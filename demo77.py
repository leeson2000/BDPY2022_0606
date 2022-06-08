def func77():
    a = 1
    for i in range(10):
        a += i
        yield a

    pass

f1 = func77()
print(next(f1))
print(next(f1))
print([i for i in f1])