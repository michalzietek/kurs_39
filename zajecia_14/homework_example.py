import requests
from geopy.geocoders import Nominatim

city = input("Podaj nazwę miasta: ")
searched_date = input("Podaj datę (RRRR-MM-DD): ")

geolocator = Nominatim(user_agent="michal_app")
location = geolocator.geocode(city)

print(location)
latitude = location.latitude
longitude = location.longitude


ulr = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
response = requests.get(url=ulr)
print(response)
print(response.json())