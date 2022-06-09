import pandas as pd
import numpy

o1 = pd.Series([20, 15, 18, 37, 25], index=['mar', 'jan', 'feb', 'may', 'apr'])
o2 = o1.reindex(['jan', 'feb', 'mar', 'apr', 'may', 'jun'])
print(o2)

o3 = pd.Series(['L', 'M', 'S'], index=[0, 5, 10])
print(o3)
o4 = o3.reindex(range(15), method='ffill')
print(o4)
o5 = pd.DataFrame(numpy.arange(16).reshape(4, 4), index=[1, 2, 3, 4],
                  columns=['Kotlin', 'Swift', 'C++', 'Java'])
o6 = o5.reindex(columns=['objC', 'Kotlin', 'Swift', 'Java', 'C++'])
print(o6)