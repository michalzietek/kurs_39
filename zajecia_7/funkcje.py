# def przywitaj_sie():
#     print("Witaj świecie")
#
#
# # przywitaj_sie()
#
#
# def sprawdz_wiek(wiek):
#     if wiek < 18:
#         print("Jesteś niepełnoletni/a")
#     else:
#         print("Możesz kupić alkohol!!")
#
#
# def sprawdz_wiek_i_przywitaj_sie(wiek, imie):
#     if wiek < 18:
#         print("Jesteś niepełnoletni/a")
#     else:
#         print("Możesz kupić alkohol!!")
#     print(f"Witaj {imie}")
#
#
# wiek_uzytkownika = int(input("Podaj swój wiek: "))
# #
# wiek_nasz = sprawdz_wiek(wiek_uzytkownika)
# print(wiek_nasz)
# # sprawdz_wiek(15)
#
# nazwa_uzytkownika = input("Podaj swoje imie: ")

# sprawdz_wiek_i_przywitaj_sie(wiek_uzytkownika, nazwa_uzytkownika)
#
# # Niepoprawne wywołanie - bez podania stricte mapowania jest kolejność naturalna
# #sprawdz_wiek_i_przywitaj_sie(nazwa_uzytkownika, wiek_uzytkownika)


# sprawdz_wiek_i_przywitaj_sie(imie=nazwa_uzytkownika, wiek=wiek_uzytkownika)

# Problematyczne wywołanie związane z kolejnością.
# sprawdz_wiek_i_przywitaj_sie(nazwa_uzytkownika, wiek=wiek_uzytkownika)


# miasta = [("Warszawa", 20, 67.6), ("Szczecin", 30, 84.8)]
#
#
# def obliczanie_temperatury_w_fahrenheitach(temperatura_w_celsjuszach):
#     temperatura_fahrenheit = temperatura_w_celsjuszach * 9 / 5 + 32
#     print(f"Temperatura w fahreinheitach: {temperatura_fahrenheit}")
#     return temperatura_fahrenheit
#
#
# temperatura_w_celsjuszach = float(input("Podaj temperaturę w celsjuszach: "))
# miasto = input("Podaj miasto: ")
#
# temperatura_nasza_fahrenheit = obliczanie_temperatury_w_fahrenheitach(
#     temperatura_w_celsjuszach
# )
#
# miasta.append((miasto, temperatura_w_celsjuszach, temperatura_nasza_fahrenheit))
#
# print(miasta)


def przywitaj_sie(imie="Michał"):
    print(f"Cześć {imie}")


przywitaj_sie()
przywitaj_sie("Kamil")
