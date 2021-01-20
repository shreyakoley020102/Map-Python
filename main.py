import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am Marker", icon=folium.Icon(color='green')))

map.save("Map1.html")
#map1 = folium.Map(location=[38.58, -99.09],zoom_start=6)
#map1.save("Map2.html")

#tiles = "Stamen Terrain"

