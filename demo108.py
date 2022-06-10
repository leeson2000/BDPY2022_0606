# 手動建一個map目錄
import folium
import requests

URL_V1 = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
URL_V2 = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

r1 = requests.get(URL_V1)
v1Dict = r1.json()["retVal"]

location = [25.040895439490978, 121.54202039785565]
map_osm = folium.Map(location=location, zoom_start=11)
for v1 in v1Dict.values():
    icon = folium.Icon(color='pink', icon='info-sign')
    folium.Marker([v1["lat"], v1["lng"]],  icon=icon, popup=None).add_to(map_osm)

map_osm.save('map/demo108.html')
