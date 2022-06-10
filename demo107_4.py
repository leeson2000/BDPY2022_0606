# 手動建一個map目錄
import folium
import pandas as pd

sampleData = pd.read_csv('data/demo107.csv', sep=',')
print(sampleData['備註'].unique())
sampleData.drop('備註', axis=1, inplace=True)
uniqueSection = sampleData['行政區'].unique()
print(uniqueSection)
#################################
icons = ['info-sign', 'question-sign', 'ok-sign', 'remove-sign', 'minus-sign', 'plus-sign',
         'remove-circle', 'ok-circle', 'ban-circle', 'play', 'pause', 'stop']
sectionDict = {}
for s, i in zip(uniqueSection, icons):
    sectionDict[s] = i
print(sectionDict)
#################################
print(sampleData['行政區'].value_counts())
print(sampleData.shape)
print(sampleData.columns)
sampleData.columns = ['section', 'road', 'road_detail', 'lon', 'lat']
location = [25.040895439490978, 121.54202039785565]
map_osm = folium.Map(location=location, zoom_start=11)

for i in range(len(sampleData)):
    coord = [sampleData.loc[i, 'lat'], sampleData.loc[i, 'lon']]
    message = "%s,%s" % (sampleData.loc[i, 'road'], sampleData.loc[i, 'road_detail'])
    icon1 = folium.Icon(color='blue', icon=sectionDict[sampleData.loc[i, 'section']])
                                      ###############################################
    folium.Marker(coord, icon=icon1, popup=message).add_to(map_osm)

map_osm.save('map/demo107.html')
