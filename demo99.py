from matplotlib import pyplot as plt
import numpy as np

X = np.arange(0, 10, 0.25)
print(X)
Y = X ** 2
Z = (X ** 2) / 3

#plt.plot(X, X, 'rs', X, Y, 'g^', X, Z, 'b--')
plt.plot(X, X, 'rs')
plt.plot(X, Y, 'g^')
plt.plot(X, Z, 'b--')
plt.axis([0, 10, 0, 90])
plt.show()