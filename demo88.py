import pandas as pd

dict1 = {'station': ['Nangang', 'Taipei', 'Banqiao', 'Taoyuan', 'Hsinchu'],
         'order': [1, 2, 3, 4, 5],
         'backOrder': [5, 4, 3, 2, 1]}
pd1 = pd.DataFrame(dict1)
print(pd1.drop(2))
print(pd1.drop([1, 3]))
print(pd1.drop('order', axis=1))
print(pd1.drop(['order', 'backOrder'], axis=1))
print(pd1.drop(['order', 'backOrder'], axis='columns'))
pd1.drop([1, 4], inplace=True)
print(pd1)