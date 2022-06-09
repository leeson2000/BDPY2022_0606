import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sequence1 = pd.DataFrame(np.random.normal(1.0, 0.07, (100, 8)))
print(sequence1.head())

accumulates = sequence1.cumprod()
print(accumulates.head())
accumulates.plot()
plt.show()