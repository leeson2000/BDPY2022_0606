import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df1)
print(df1.sum())
print(df1.sum(axis='columns'))
df1.iloc[2, 3] = np.NaN
print(df1)
print(df1.sum())
print(df1.sum(axis='columns'))
print("***" * 50)
print(df1.sum(skipna=False))
print(df1.sum(skipna=False, axis='columns'))
print("***"*50)
print(df1.idxmax())
print(df1.idxmin())
print(df1.idxmax(axis='columns'))
print(df1.idxmin(axis='columns'))
print(df1)
print(df1.cumsum())
print(df1.cummax())
print(df1.describe())