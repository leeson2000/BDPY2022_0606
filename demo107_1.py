# 手動建一個map目錄
import folium
import pandas as pd

sampleData = pd.read_csv('data/demo107.csv', sep=',')
print(sampleData['備註'].unique())
sampleData.drop('備註', axis=1, inplace=True)
print(sampleData['行政區'].unique())
print(sampleData['行政區'].value_counts())
print(sampleData.shape)
print(sampleData.columns)
sampleData.columns = ['section', 'road', 'road_detail', 'lon', 'lat']
location = [25.040895439490978, 121.54202039785565]
map_osm = folium.Map(location=location, zoom_start=11)
map_osm.save('map/demo107.html')
