"""
**Zadanie: Napisz program, który dostarczy informacji o wybranym kraju. Użyj do tego poniższego API Rest Countries. Aplikacja ma działać następująco:**
• Program pyta użytkownika o nazwę kraju, dla którego należy sprawdzić informacje. Nazwa kraju musi być podana w języku angielskim i pozwala na pełne lub częściowe dopasowanie.
• Aplikacja wykona zapytanie do API w celu pozyskania danych o kraju.
• Program powinien wyświetlić następujące informacje o kraju (jeżeli są dostępne):
    ◦ Pełna nazwa kraju
    ◦ Stolica
    ◦ Region
    ◦ Podregion
    ◦ Populacja
    ◦ Języki urzędowe
    ◦ Waluta
    ◦ Flagę (poprzez URL do obrazka)
• Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukany kraj znajduje się już w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.
URL do API:
https://restcountries.com/v3.1/name/{country_name}?fullText=true
W URL należy uzupełnić parametr: country_name
Przykładowy funkcjonalny rezultat dla zapytania "Poland":
Pełna nazwa: Republic of Poland
Stolica: Warsaw
Region: Europe
Podregion: Eastern Europe
Populacja: 37970000
Języki urzędowe: Polish
Waluta: Polish złoty (PLN)
Flaga: https://flagcdn.com/pl.svg
**Wskazówka:** Możesz wymagać od użytkownika podania pełnej nazwy kraju (ustawiając parametr fullText na true w URL) lub pozwolić na wyszukiwanie zarówno pełnych, jak i częściowych nazw kraju (bez parametru fullText).
"""
from file_handler import FileHandler
import requests

file_handler = FileHandler("data.json")

def get_data_from_countries_api(country):
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Niestety taki kraj nie istnieje.")

def modify_data_from_api_to_our_dict(response_data):
    country_info = response_data[0]
    result = {
        "full_name": country_info.get("name", {}).get("common", "N/A"),
        "capital": country_info.get("capital", ["N/A"]),
        "region": country_info.get("region", "N/A"),
        "subregion": country_info.get("subregion", "N/A"),
        "population": country_info.get("population", "N/A"),
        "languages": country_info.get("languages", {}),
        "currency": country_info.get("currencies", {}),
        "flag": country_info.get("flags", {}).get("svg", "N/A")
    }
    return result

# user_country = input("Podaj nazwę kraju w języku angielskim: ")
# if country := file_handler.check_country_exists(user_country):
#     print("Kraj znajduje się już w pliku. Oto jego dane:")
#     print(country)
# else:
#     response_data = get_data_from_countries_api(user_country)
#
#     modified_data = modify_data_from_api_to_our_dict(response_data)
#
#     file_handler.data.append(modified_data)
#     file_handler.write_file()

print(file_handler["Norway"])

# file_handler["Sweden"] = {"name": "Germany"}

# for country in file_handler:
#     print(country)

my_generator = file_handler.items()

for item in my_generator:
    print(item)