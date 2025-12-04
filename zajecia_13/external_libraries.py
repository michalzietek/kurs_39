import requests

response = requests.get("https://www.sport.pl")
print(response.text)