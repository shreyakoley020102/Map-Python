import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

#map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am Marker", icon=folium.Icon(color='green')))

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1],[36.2, -98.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am Marker", icon=folium.Icon(color='green')))

#fg.add_child(folium.Marker(location=[37.2, -97.1], popup="Hi I am Marker", icon=folium.Icon(color='green')))

map.add_child(fg)


map.save("Map1.html")
#map1 = folium.Map(location=[38.58, -99.09],zoom_start=6)
#map1.save("Map2.html")

#tiles = "Stamen Terrain"

