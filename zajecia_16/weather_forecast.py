import json

class WeatherForecast:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def __getitem__(self, item):
        city, date = item
        for searched_city, data in self.data.items():
            if city == searched_city:
                for searched_date, info in data.items():
                    if searched_date == date:
                        return info


    def __setitem__(self, key, value):
        city, date = key
        if city not in self.data.keys():
            self.data[city] = {}
        self.data[city][date] = value
        print(self.data)



weather_forecast = WeatherForecast("struktura_danych.json")

# print(weather_forecast.data)

print(weather_forecast["Szczecin", "2025-12-10"])

weather_forecast["Szczecin", "2025-12-15"] = "pada"
weather_forecast["Poznań", "2025-12-15"] = "pada"