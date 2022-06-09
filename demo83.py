import pandas as pd

d1 = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
      'year': [2018, 2017, 2019, 2020],
      'slide': [200, 250, 230, 300]}
df1 = pd.DataFrame(d1)
print(type(df1), type(d1))
print(d1)
print(df1)
df2 = pd.DataFrame(d1, columns=['course', 'slide', 'year', 'instructor'])
print(df2)

df3 = pd.DataFrame(d1, columns=['course', 'slide', 'year', 'instructor'], index=['p1', 'p2', 'p3', 'p4'])
print(type(df3.loc['p1']))
print(df3.loc['p1'])
print(df3.loc['p1'].index)
print(df2.loc[0])
print("slice 2 rows from datafrmae")
print(type(df3.loc[['p1', 'p3']]))
print(df3.loc[['p1', 'p3']])
print(df2.loc[[0, 2]])
print("loc and iloc")
print(df2.iloc[0])
print(df3.iloc[0])
print("--- loc and iloc2 ---")
print(df2.iloc[[0, 2]])
print(df3.iloc[[0, 2]])