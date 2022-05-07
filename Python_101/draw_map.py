import geocoder
import folium

location = geocoder.osm('國立高雄師範大學').latlng
print(location)

