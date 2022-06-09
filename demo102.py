import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2)
axes[0, 0].hist(np.random.randn(50), bins=10, color='c', alpha=1)
axes[1, 1].scatter(np.arange(30), np.arange(30)+3*np.log(10)*np.random.randn(30))
plt.show()