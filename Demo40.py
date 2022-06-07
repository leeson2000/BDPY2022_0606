import math
import random

print(math.pi, math.e, math.sin(0), math.sin(math.pi / 2))
print(math.log(2, 10), math.log10(2))
print(math.log(3, 10), math.log10(3))
print(math.log2(8), math.log(8, 2))
for _ in range(10):
    print(random.randint(0, 5), end=" ")
print()
lunches = ['7-11', 'fami', 'hi-life', 'OK', 'PXMart']
for _ in range(5):
    print(random.choice(lunches))

for _ in range(5):
    print(random.sample(lunches, 3))

cards = ['A', 'K', 'Q', 'J', '10', '9']
for _ in range(5):
    random.shuffle(cards)
    print(cards)