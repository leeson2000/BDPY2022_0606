import pandas as pd

stations1 = ['nangang', 'taipei', 'banqiao', 'taoyuan']
stations2 = ['hsinchu', 'taichung', 'tainan']
s1 = pd.Series([1000, 800, 500, 300], index=stations1)
s2 = pd.Series([500, 300, 400], index=stations2)
s3 = pd.Series([2000, 1000, 800, 200], index=stations1)
s4 = pd.Series([600, 400, 500], index=stations2)
print(s1)
print(s2)
print(s1 + s2)
print("---" * 30)
print(s1 + s3)
print(s2 + s4)
print("---" * 30)
s5 = pd.concat((s1, s2))
s5.name = 'ticket sold'
s5.index.name = 'station'
print(s5)
# change index directly, without re-order data
# s5.index = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
s5.index = ['hsinchu', 'taichung', 'tainan', 'nangang', 'taipei', 'banqiao', 'taoyuan']
print(s5)