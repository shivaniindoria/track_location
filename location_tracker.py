import phonenumbers
from phonenumbers import geocoder,carrier

from opencage.geocoder import OpenCageGeocode
import folium
number = input('enter number (with country code): ')
key = 'ba855b820d7e4377ba37dd6f4102748b'
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,'en')
print(number_location)
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))

geocoder =OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lattitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print(lattitude,longitude)

map_location = folium.Map(location=[lattitude,longitude],zoom_start=9)
folium.Marker([lattitude,longitude],popup=number_location).add_to(map_location)
map_location.save('location.html')
print('open location.html file in browser or copy and paste below link in browser')
print('http://localhost:5500/location.html')
