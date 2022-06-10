import pandas as pd

df1 = pd.read_csv('data/demo106.csv')
print(df1.shape)
print(df1.head())
print(df1.columns)
print(df1.info())
view1 = df1[['處分字號', '違反勞動基準法條款']].groupby(['違反勞動基準法條款']) \
    .count().sort_values('處分字號', ascending=False)
print(view1.head())
view2 = df1[['處分字號', '違反勞動基準法條款','違反法規內容']].groupby(['違反勞動基準法條款','違反法規內容']) \
    .count().sort_values('處分字號', ascending=False)
print(view2.head())