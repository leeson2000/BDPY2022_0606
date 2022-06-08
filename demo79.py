import pandas as pd

pd1 = pd.Series([3, 1, 4, 5, 9, -2, 8])
print(type(pd1))
print(pd1)
print(pd1.values)
print(pd1.index)

pd2 = pd.Series([4, 7, -5, 3], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
print(pd2)
print(pd2.values)
print(pd2.index)
print(pd1[0], pd1[2], pd1[3])
print(pd2['nangang'], pd2['taipei'], pd2['banqiao'])
print(pd1[[0, 2, 3]])
print(pd2[['nangang', 'taipei', 'banqiao']])
print(pd2 > 0)
print(pd2[pd2 > 0])
print(pd2 ** 2)