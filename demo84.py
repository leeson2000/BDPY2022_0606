import pandas as pd

d1 = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
      'year': [2018, 2017, 2019, 2020],
      'slide': [200, 250, 230, 300]}
df1 = pd.DataFrame(d1)
print(df1)
s1 = pd.Series(['taipei', 'hsinchu', 'taichung', 'kaohsiung'], index=[0, 1, 2, 3])
print(s1)
df1['location'] = s1
print(df1)
s2 = pd.Series(['remote', 'local'], index=[0, 3])
df1['method'] = s2
print(df1)
df1['heavy'] = df1['slide'] > 250
print(df1)
del df1['slide']
print(df1)