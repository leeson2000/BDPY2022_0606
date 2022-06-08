class MyContainer():
    def __init__(self):
        print("init")
        self.counter = 1

    def __iter__(self):
        print("iter")
        return self

    def __next__(self):
        print("next")
        self.counter += 1
        if self.counter>10:
            raise StopIteration
            #raise StopIteration()
        return self.counter


c1 = MyContainer()
# print(c1.counter)
# print(next(c1))
# print(next(c1))
# print(next(c1))

for i in c1:
    print(i)