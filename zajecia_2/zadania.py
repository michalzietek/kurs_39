""" """

# Zadanie 1 — Porównanie wieku
"""
Poproś użytkownika o dwa wieki (liczby całkowite): wiek Michała i wiek Ani.
Wypisz:
1) czy Michał jest starszy od Ani,
2) czy Ania jest młodsza lub równa wiekiem Michałowi,
3) czy mają tyle samo lat.
Użyj operatorów: >, <=, ==.
"""

# wiek_michala = int(input("Podaj wiek Michała: "))
# wiek_ani = int(input("Podaj wiek Ani: "))
#
# print(f"Czy Michał jest starszy od Ani? {wiek_michala > wiek_ani}")
# print(f"Czy Ania jest młodsza lub równa Michałowi? {wiek_michala >= wiek_ani}")
# print(f"Czy mają tyle samo lat? {wiek_michala == wiek_ani}")

# Zadanie 2 — Porównanie cen owoców
"""
Poproś użytkownika o trzy ceny (liczby zmiennoprzecinkowe w zł): jabłka, pomarańczy i banana.
Wypisz:
1) czy jabłko jest tańsze od pomarańczy,
2) czy pomarańcza jest droższa od banana,
3) czy jabłko i banan kosztują tyle samo,
4) czy jabłko jest tańsze od pomarańczy lub równe bananowi,
5) czy pomarańcza jest droższa od jabłka i banana jednocześnie.
"""

#
# cena_jablka = float(input("Podaj cene jablka: "))
# cena_pomaranczy = float(input("Podaj cene pomaranczy: "))
# cena_banana = float(input("Podaj cene banana: "))
#
# print(f"Jabłko tańsze od pomarańczy: {cena_jablka < cena_pomaranczy}")
# print(f"Pomarańcza droższa od banana: {cena_banana < cena_pomaranczy}")
# print(f"Jabłko i banan kosztują tyle samo: {cena_jablka == cena_pomaranczy}")
# print(f"Jabłko tańsze od pomarańczy lub równe bananowi: {cena_jablka < cena_pomaranczy or cena_jablka == cena_banana}")
# print(f"Pomarańcza droższa od banana i jabłka: {cena_jablka < cena_pomaranczy and cena_banana < cena_pomaranczy}")

# Zadanie 3 — Logiczne fakty o pogodzie
"""
Poproś użytkownika o 3 wartości logiczne jako 0 lub 1:
- jest_cieplo
- pada_deszcz
- wieje_wiatr

Wypisz:
1) czy jest dobra pogoda na spacer (ciepło i nie pada),
2) czy lepiej zostać w domu (nie jest ciepło lub pada),
3) czy pada albo wieje,
4) czy nie pada,
5) czy jest ciepło, ale nie pada i nie wieje.
"""
#
# jest_cieplo = bool(int(input("Czy jest cieplo?")))
# pada_deszcz = bool(int(input("Czy pada deszcz?")))
# wieje_wiatr = bool(int(input("Czy wieje wiatr?")))
#
# print(f"Dobra pogoda na spacer?{jest_cieplo and not pada_deszcz}")
# print(f"Lepiej zostać w domu?{not jest_cieplo or pada_deszcz}")
# print(f"Pada albo wieje?{pada_deszcz or wieje_wiatr}")
# print(f"Nie pada?{not pada_deszcz}")
# print(f"Jest ciepło, nie pada i nie wieje?{jest_cieplo and not pada_deszcz and not wieje_wiatr}")


# Zadanie 4 — Typy i konwersje z wejścia
"""
Poproś użytkownika o wiek (tekst) i wagę (tekst, np. '72.5').
Następnie:
- skonwertuj wiek na int, wagę na float,
- dodaj 5 do wieku,
- dodaj 2.3 do wagi,
- wypisz nowe wartości oraz ich typy.
"""

# wiek = int(input("podaj wiek: "))
# waga = float(input("podaj wagę: "))
#
# # wiek = wiek + 5
# # waga = waga + 2.3
#
# wiek += 5
# waga += 2.3
#
# print(f"Waga: {waga} typ: {type(waga)}")
# print(f"Wiek: {wiek} typ: {type(wiek)}")

# Zadanie 5 — Cukierki dla dzieci
"""
Poproś użytkownika o liczbę cukierków i liczbę dzieci.
Policz i wypisz:
- ile cukierków dostanie każde dziecko (//),
- ile cukierków zostanie (%),
- czy cukierków wystarczy dla wszystkich dzieci (cukierki >= dzieci),
- czy cukierków jest mniej niż 10 lub więcej niż 100.
"""

# cukierki = int(input("Podaj liczbę cukierków"))
# dzieci = int(input("Podaj liczbę dzieci"))
#
# na_dziecko = cukierki // dzieci
# reszta_z_dzielenia = cukierki & dzieci
#
# print(f"Jedno dziecko dostanie: {na_dziecko}")
# print(f"Zostanie: {reszta_z_dzielenia}")
# print(f"Czy cukierków wystarczy na wszystkie dzieci? {cukierki >= dzieci}")
# print(f"Czy cukierków jest mniej niż 10 lub więcej niż 100? {cukierki < 10 or cukierki > 100}")

# Zadanie 6 — Koszyk PRO: budżet i logika zakupów
"""
Poproś użytkownika o:
- cenę i liczbę sztuk trzech produktów (A, B, C),
- dostępny budżet w zł.

Oblicz i wypisz:
1) łączną wartość koszyka,
2) czy mieści się w budżecie,
3) czy istnieje para produktów o tej samej cenie,
4) czy łączna liczba sztuk > 10,
5) czy żadna cena nie jest 0,
6) czy budżet wystarcza i wszystkie ceny > 0,
7) czy jakiś produkt jest co najmniej 2× droższy od innego.
"""

cena_A = float(input("Cena produktu A (zł): "))
sztuki_A = int(input("Liczba sztuk produktu A: "))

cena_B = float(input("Cena produktu B (zł): "))
sztuki_B = int(input("Liczba sztuk produktu B: "))

cena_C = float(input("Cena produktu C (zł): "))
sztuki_C = int(input("Liczba sztuk produktu C: "))

budzet = float(input("Podaj swój budżet (zł): "))

suma = cena_A * sztuki_A + cena_B * sztuki_B + cena_C * sztuki_C

print(f"Suma zakupów: {suma}")
print(f"Suma większa od budżetu? {suma > budzet}")

print(
    f"Para produktów o tej samej cenie? {cena_A == cena_B or cena_A == cena_C or cena_B == cena_C}"
)

print(f"Powyżej 10 sztuk? {sztuki_C + sztuki_B + sztuki_A > 10}")

print(f"Czy jakaś cena jest równa 0? {cena_C == 0 or cena_B == 0 or cena_A == 0}")

print(
    f"Budżet wystarczający i ceny powyżej 0? {budzet > suma and cena_C > 0 and cena_A > 0 and cena_B > 0}"
)

print(
    f"Jeden produkt 2x droższy od drugiego? {
        (cena_A >= 2 * cena_B)
        or (cena_A >= 2 * cena_C)
        or (cena_B >= 2 * cena_A)
        or (cena_B >= 2 * cena_C)
        or (cena_C >= 2 * cena_A)
        or (cena_C >= 2 * cena_B)
    }"
)

# Zadanie 7 — Bilety, zniżka i warunki zakupu
"""
Poproś użytkownika o:
- cenę jednego biletu,
- liczbę biletów,
- procent zniżki,
- kwotę w portfelu,
- maksymalną akceptowalną cenę za 1 bilet po zniżce.

Oblicz:
- koszt całkowity po zniżce,
- cenę 1 biletu po zniżce.

Wypisz:
1) koszt po zniżce,
2) czy użytkownika stać na zakup,
3) czy zniżka jest co najmniej 15%,
4) czy liczba biletów jest parzysta,
5) czy cena 1 biletu po zniżce ≤ limit,
6) warunek złożony: stać na zakup oraz (zniżka ≥15% lub liczba biletów parzysta).
"""
