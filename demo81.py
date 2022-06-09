import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz': 28, 'testit': 14}
l1 = ['andbiz2', 'testit', 'poop', 'bdpy']
s1 = pd.Series(d1, index=l1)
print(s1)
l2 = ['andbiz2', 'testit', 'anbiz', 'poop', 'andbiz3', 'bdpy']
s2 = pd.Series(d1, index=l2)
print(s2)
print("is na??")
print(pd.isna(s2))
print("is missing value?")
print(pd.isnull(s2))
print("is na2(using s2)??")
print(s2.isna())
print(s2.isnull())
print("---" * 30)
d2 = {'poop': 'Mark', 'bdpy': None, 'andbiz2': None, 'testit': 'Frank'}
s3 = pd.Series(d2, index=l2)
print(s3)
print("****"*30)
print(s3.isna())
print("****"*30)
print(s3.isnull())