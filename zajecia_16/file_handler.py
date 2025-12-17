import json

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()

    def read_file(self):
        with open(self.filename, 'r') as file:
            return json.loads(file.read())

    def write_file(self):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.data, indent=4))

    def check_country_exists(self, country_name):
        for country in self.data:
            if country.get("full_name").lower() == country_name.lower():
                return country

    def __getitem__(self, item):
        for country in self.data:
            if country.get("full_name") == item:
                return country
        return "Nie ma takiego kraju w naszym programie!"

    def __setitem__(self, key, value):
        print(f"Klucz: {key}")
        print(f"Wartość: {value}")
        for country in self.data:
            if country.get("full_name") == key:
                self.data.remove(country)
        self.data.append({"full_name": key, **value})
        self.write_file()

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for country in self.data:
            yield f"{country.get('full_name')}: {country}"