import pandas as pd

d1 = {'poop': {2019: 5, 2020: 8},
      'bdpy': {2018: 5, 2019: 7, 2020: 10}}
df1 = pd.DataFrame(d1)
print(df1)
df2 = df1.T
print(df2)
df3 = pd.DataFrame(d1, index=[2018, 2019, 2020, 2021])
print(df3)
print(type(df3.values))
print(df3.values)

d2 = {'poop': {2019: 5, 2020: 8},
      'bdpy': {2018: 5, 2019: 7, 2020: 'not yet receive'}}
df4 = pd.DataFrame(d2, index=[2018, 2019, 2020, 2021])
print(df4.values)
print(type(df4.values))
print(df4.values[0, 0], df4.values[0, 1], df4.values[2, 0], df4.values[2, 1])
print(type(df4.values[0, 0]), type(df4.values[0, 1]), type(df4.values[2, 0]), type(df4.values[2, 1]))