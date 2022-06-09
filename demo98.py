import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
a1 = np.array(l1)
a2 = np.array(l2)
print(a1 + a2, a1 - a2, a1 * a2, a1 / a2)
print(a1.mean(), a1.std(), a1.max(), a1.min())