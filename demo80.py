import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz': 28, 'testit': 14}
print(type(d1))
pd1 = pd.Series(d1)
print(pd1)
print('poop' in d1, 'poop' in pd1)
print(d1['poop'], pd1['poop'])
print(f"dict: keys={d1.keys()}, value={d1.values()}")
print(f"series keys={pd1.index}, value={pd1.values}")
# print(d1["xxxxxx"])
# print(pd1['XXXXXX'])
queriesKeys = ['xyz', 'poop', 'bdpy', 'C#', 'testit','power bi']
for k in queriesKeys:
    print(f"key {k} in pd1? if yes, return object, if false, return false==>{k in pd1 and pd1[k]}")