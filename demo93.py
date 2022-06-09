import pandas as pd

s1 = pd.Series([4, -15, 7, 7, 2, 2, 0, 0, 4])
print(s1.rank())
print(s1.rank(method='first'))
print(s1.rank(method='max'))
print(s1.rank(method='min'))