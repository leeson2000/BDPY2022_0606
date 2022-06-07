import itertools

x1 = "abc"
x2 = '123'
x3 = "甲乙丙丁"

c1 = itertools.chain(x1, x2, x3)
print(c1)
# print(next(c1))
# print(next(c1))
# print(next(c1))
print(list(c1))
#c1 = itertools.chain(x1, x2, x3)
print(list(c1))

c2 = itertools.chain(x1, x2, x3, x3, x2, x1)
t2 = tuple(c2)
print(len(t2))
print(t2)
print(t2)
p1 = tuple(itertools.permutations(x3, 2))
print(len(p1), p1)
c1 = tuple(itertools.combinations(x3, 2))
print(len(c1), c1)