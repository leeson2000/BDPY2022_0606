import pandas

df1 = pandas.read_csv('data/demo105.csv', skiprows=4, index_col='Country Name')
print(df1.drop('Indicator Name', axis=1, inplace=True))
print(df1.drop('Indicator Code', axis=1, inplace=True))
print(df1.drop('Unnamed: 66', axis=1, inplace=True))
print(df1.columns)
print(df1.shape)
print(df1.head())
df1.to_excel('data/demo105_output.xlsx', sheet_name="population")