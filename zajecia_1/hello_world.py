"""
AUTOR PROGRAMU: Michał Ziętkowski
DATA: 20.10.2025
FIRMA: Future Collars
"""

# print("Hello world")
#
# ########### ZMIENNE LICZBOWE
#
# wiek = 30 # typ integer
#
# print(wiek)
#
# wiek = 20 + 5 #dodawanie
#
# wiek2 = 30 - 1 #odejmowanie
#
# wiek3 = 5 * 6 #mnozenie
#
# wiek4 = 120 / 4 #dzielenie zwraca typ float
#
# kwadrat_wieku = 5**2 #potęgowanie
#
# cena_jabka = 2.99 # typ float
#
# ilosc_jablek = 0.66
#
# modulo = 6 % 4 # reszta z dzielenia
#
# wiek_float = 30.0 + 6
#
# print(wiek)
# print(wiek2)
# print(wiek3)
# print(wiek4)
# print(kwadrat_wieku)
# print(modulo)
# print(wiek_float)
#
#
# wartosc_jablek = cena_jabka * ilosc_jablek
#
# wartosc_jablek_2 = cena_jabka * 1.2
#
# print(wartosc_jablek)
# print(round(wartosc_jablek))

################# ZMIENNE TEKSTOWE

# imie = "Michał"
# imie_2 = 'Michał'
#
# tekst_piosenki = """
# To jest nasz tekst piosenki, lalaalalalalalalalaa.
# Zwrotka 1
# tgsdgdfgedfgh
# """
# print(imie)
# print(imie_2)
#
# print(tekst_piosenki)
#
# zlozona_wiadomosc = f"Imię: {imie}"
# print(zlozona_wiadomosc)
#
# print(f"Witaj w swiecie programowania: {imie}")
#
# nazwisko = "Ziętkowski"
#
# nazwisko_1 = nazwisko.lower()
# nazwisko_1 = nazwisko.upper()
# nazwisko_1 = nazwisko.capitalize()
#
# print(nazwisko_1)
#
# imie_i_nazwisko = imie + " " + nazwisko
#
# print(imie_i_nazwisko)

# "Wiadomosc {pierwsza_zmienna}".format(pierwsza_zmienna=imie)

######## ZMIENNE BOOLEAN

czy_jestem_pelnoletni = True

czy_jestem_na_emeryturze = False

# print(czy_jestem_na_emeryturze and czy_jestem_pelnoletni)


cena_jablka = 2.99

cena_pomidora = 3.49

cena_winogrona = 3.49

# print(cena_jablka > cena_pomidora)
# print(cena_jablka < cena_pomidora)
# print(cena_jablka != cena_pomidora)
# print(cena_jablka == cena_pomidora)
# print(cena_winogrona >= cena_pomidora)
# print(cena_winogrona <= cena_pomidora)


# print(czy_jestem_pelnoletni or czy_jestem_na_emeryturze)
#
# print(not czy_jestem_na_emeryturze)
# print(not czy_jestem_pelnoletni)

print("michal" != "michal")

dzielenie = 120 / 4.5

print(dzielenie)

print(type(dzielenie))

dzielenie_integer = int(dzielenie)

print(dzielenie_integer)
print(type(dzielenie_integer))

imie = "Michal"

wiek_string = "30"

wiek_int = int(wiek_string)

wiek_float = float(wiek_string)

# wiek_float = float(wiek_int)

# print(wiek_int)
#
# print(bool(0))
# print(bool(1))
# print(bool(2))
# print(bool(-1))
# print(bool(0.000000000000001))

print(type(wiek_float))
print(type(wiek_string) is str)


######## ZMIENNA NONE

zmienna_niezdefiniowana = None

print(type(zmienna_niezdefiniowana))

zmienna_niezdefiniowana = "Adam"

print(type(zmienna_niezdefiniowana))


########## OPERACJA WEJŚCIA

# imie_uzytkownika = input("Podaj swoje imię: ")
# nazwisko_uzytkownika = input("Podaj swoje nazwisko: ")
#
# wiek_uzytkownika = input("Podaj swój wiek (liczby całkowite): ")
# is_wiek_a_number = (print(wiek_uzytkownika.isdigit()))
#
#
# print(f"Stworzyliśmy użytkownika {imie_uzytkownika} {nazwisko_uzytkownika}, który ma {wiek_uzytkownika} lat.")
#
# print(type(imie_uzytkownika))
# print(type(nazwisko_uzytkownika))
# print(type(wiek_uzytkownika))

### ZMIENNE TEKSTOWE v2

tekst_o_michale = "był sobie ktoś imieniem: 'Michał' "
print(tekst_o_michale)

print(imie)


# obecny_rok = 2025
#
# rok_urodzenia = int(input("Podaj rok: "))
#
# wiek = obecny_rok - rok_urodzenia

import datetime


obecny_rok = datetime.datetime.now().year

print(obecny_rok)
