# 手動建一個map目錄
import folium

location = [25.040895439490978, 121.54202039785565]
map_osm = folium.Map(location=location, zoom_start=13)
map_osm.save('map/demo107.html')