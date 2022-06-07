l1 = ['a', 'b', 'c']
l2 = "abc"
print([l for l in l1])
print([l for l in l2])
l1[0]='A'
#l2[0]='X'

class Person(object):
    def __init__(self, age):
        self.age = age


p = Person(5)
x = 5
print(f"p.age={p.age}, x={x}")
print(f"p id={hex(id(p))}")
print(f"x id={hex(id(x))}")
p.age = 6
x = 6
print(f"p.age={p.age}, x={x}")
print(f"p id={hex(id(p))}")
print(f"x id={hex(id(x))}")
print(p.age == x)
print(p.age is x)
y1 = [1, 2, 3]
y2 = [1, 2, 3]
y3 = y1
print(y1 == y2, y1 is y2)
print(y1 == y3, y1 is y3)