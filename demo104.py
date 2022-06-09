from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

mu = 80
sigma = 8
num_beans = 50
x = mu + sigma * np.random.randn(100000)
print(len(x))
n, bins, patches = plt.hist(x, num_beans, density=1, facecolor='blue', alpha=0.5)
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r*-')
plt.show()