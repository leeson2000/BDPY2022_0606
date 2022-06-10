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

for i in range(len(sampleData)):
    # coord = [sampleData.iloc[i, 4], sampleData.iloc[i, 3]]
    coord = [sampleData.loc[i, 'lat'], sampleData.loc[i, 'lon']]
    icon1 = folium.Icon(color='blue', icon='info-sign')
    folium.Marker(coord, icon=icon1, popup=None).add_to(map_osm)
    # print(f"coord={coord}")

map_osm.save('map/demo107.html')