uczen_1 = "Adam Adamkiewicz"
uczen_2 = "Bartek Baran"
uczen_3 = "Cezary Czkawka"
uczen_4 = "Elżbieta Elska"

#TWORZENIE

lista_uczniow = ["Adam Adamkiewicz", "Bartek Baran", "Cezary Czkawka", "Damian Dąbrowski", "Cezary Czkawka"]
print(type(lista_uczniow))
lista_uczniow_2 = [uczen_1, uczen_2, uczen_3, uczen_4]
print(type(lista_uczniow_2))
lista_wartosci = ["Jabłko", 1, True, 23.5, None]
lista_inny_sposob = list()
lista_na_pozniej = []

#ODCZYTYWANIE
# print(lista_wartosci)
# print(lista_uczniow[0])
# print(lista_uczniow[1])
# # print(lista_uczniow_2[2])
# print(lista_uczniow.index("Cezary Czkawka"))
# cezary = lista_uczniow[lista_uczniow.index("Cezary Czkawka")]
# print(cezary)
# for uczen in lista_uczniow:
#     if uczen == "Cezary Czkawka":
#         print("Znalazłem Cezarego!")
#     print(uczen)
#
# for index, uczen in enumerate(lista_uczniow):
#     if uczen == "Cezary Czkawka":
#         print(f"Cezary znaleziony pod indeksem: {index}")
#         index_cezarego = index

#DODAWANIE WARTOŚCI
print(lista_uczniow)
lista_uczniow.append("Andrzej Fleja")
print(lista_uczniow)

lista_uczniow.insert(1, "Jędrzej Jakiś")
print(lista_uczniow)

lista_uczniow.insert(100, "Zenon Ziębicki")
print(lista_uczniow)
print(len(lista_uczniow))

imie = "Michał"
imie = "Adam"
# ZMIANA WARTOŚCI
lista_uczniow[0] = "Adam Górski"
print(lista_uczniow)

lista_adamow = ["Adam Adamkiewicz", "Adam Adamkiewicz", "Adam Adamkiewicz", "Adam Adamkiewicz"]

for index, adam in enumerate(lista_adamow):
    lista_adamow[index] = "Adam Górski"

print(lista_adamow)

# USUWANIE

# lista_uczniow.remove("Jędrzej Jakiś")
#
# del lista_uczniow[0]

print(lista_uczniow)

print(lista_uczniow[-1])
print(lista_uczniow[-2])

lista_uczniow.insert(-1, "Kasia")
print(lista_uczniow)

lista_w_liscie = [1, 2, [1, 2, 3]]
print(lista_w_liscie)


print(lista_uczniow[1:5:2])