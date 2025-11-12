uczen = ["Michał", "Ziętkowski", 30, True, [1, 2, 3]]

uczen_slownik = {
    "imie": "Michał",
    "nazwisko": "Ziętkowski",
    "wiek": 30,
    "czy_obecnie_stdiuje": True,
    "oceny": [1, 2, 3],
    # "imie": "Kamil",
    # [1, 2]: "test1"# unhashable type: 'list'
}
# POBIERANIE DANYCH
# print(uczen_slownik)
# print(uczen_slownik["imie"])
# # print(uczen_slownik["klasa"])
# print(uczen_slownik.get("klasa"))
# print(uczen_slownik.get("klasa", "Brak klasy w słowniku"))
#
# # DODAWANIE / ZMIANA DANYCH
# uczen_slownik["imie"] = "Kamil"
# uczen_slownik["klasa"] = "3A"
# print(uczen_slownik)
# print(uczen_slownik.get("imie"))
#
# # USUWANIE DANYCH
# del uczen_slownik["wiek"]
# print(uczen_slownik)
#
# zmienna = uczen_slownik.pop("czy_obecnie_stdiuje")
#
# print(uczen_slownik)

# ITERACJA PO SŁOWNIKU
# for element in uczen_slownik:
#     print(element)
#
# for element in uczen_slownik.keys():
#     print(element)

for value in uczen_slownik.values():
    print(value)

for klucz, wartosc in uczen_slownik.items():
    print(f"{klucz}: {wartosc}")
