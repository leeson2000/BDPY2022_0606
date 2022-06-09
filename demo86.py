import pandas as pd
import numpy as np

l1 = ['p', 'q', 'r', 's', 't']
s1 = pd.Series(range(5), index=l1)
print(s1)
print(s1.index)
i1 = pd.Index(l1, dtype='object')
print(type(i1))
print(i1)
print(i1[:3], i1[3:])

i2 = pd.Index(np.arange(4))
i3 = list(np.arange(4))
print(i2, i3)

data = ['Nangang', 'Taipei', 'Banqiao', 'Taoyuan']
s2 = pd.Series(data, index=i2)
s3 = pd.Series(data, index=i3)
print(s2)
print(s3)
print(2 in i2, 2 in i3)
i4 = pd.Index(['Taipei', 'Taipei', 'Taipei', 'Taoyuan'])
s4 = pd.Series(data, index=i4)
print(s4)
print(s4['Taipei'])