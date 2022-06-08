def func76():
    x = 123
    y = 45
    z = 67
    y = yield x + y
    yield y + z

f1 = func76()
print(next(f1))
print(f1.send(33))