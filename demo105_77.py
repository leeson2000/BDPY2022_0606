import pandas
from matplotlib import pyplot as plt, rc

df1 = pandas.read_csv('data/demo105.csv', skiprows=4, index_col='Country Name')
df1.drop('Indicator Name', axis=1, inplace=True)
df1.drop('Indicator Code', axis=1, inplace=True)
df1.drop('Unnamed: 66', axis=1, inplace=True)
# print(df1.columns)
# print(df1.shape)
# print(df1.head())
# df1.to_excel('data/demo105_output.xlsx', sheet_name='population')
print(df1['1960'].mean())
print(df1['1970'].median())
df1['80_90'] = df1['1980'] + df1['1990']
print(df1.columns)

# display
print(plt.style.available)
for style in plt.style.available:
    plt.style.use(style)
    font = {'family': 'Source Code Pro'}
    rc('font', **font)
    ausData = df1[df1['Country Code'] == "AUS"]
    print(ausData.shape)
    years = ['1960', '1970', '1980', '1990']
    ausData.plot(kind='bar', y=years, figsize=(12, 6), fontsize=14)
    plt.xticks([])
    plt.title("Aus data with 60-90 years")

    plt.show()