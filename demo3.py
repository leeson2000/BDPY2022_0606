import math

x = 5
y = 3.0
z = 5 + 3j
print(type(x), type(y), type(z))
print(z.real, z.imag)
t = 4 - 2j
print(z + t, z - t, z * t, z / t)
# 5**2-3**2
# 2*5*3
print(z ** 2)
print(abs(z))
print(math.sqrt(z.real ** 2 + z.imag ** 2))