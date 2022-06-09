import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df1)
print("below two statements are equal")
print(df1.iloc[2])
print(df1.loc[4])
print("try range")
print(df1.iloc[2:4])
print(df1.loc[4:6])
print("try 2d range")
print(df1.iloc[2:4, 2:4])
print(df1.loc[4:6, 2:3])
print("slice using iloc")
print(df1.iloc[:3])
print(df1.iloc[3:5])
print(df1.iloc[5:])
print("slice using loc")
print(df1.loc[:4])
print(df1.loc[6:8])
print(df1.loc[10:])