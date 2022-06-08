import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz': 28, 'testit': 14}
print(type(d1))
pd1 = pd.Series(d1)
print(pd1)
print('poop' in d1, 'poop' in pd1)
print(d1['poop'], pd1['poop'])