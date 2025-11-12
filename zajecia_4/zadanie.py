# Napisz program, który policzy statystyki dotyczące ocen studentów.
#
# Program działa tak:
#   1) Pyta użytkownika: "Ile ocen chcesz podać?"
#   2) Wczytuje kolejno oceny (każda w osobnej linii)
#
# ZASADY:
# - Ocena może być od 2 do 5 (włącznie).
# - Jeśli użytkownik poda ocenę spoza zakresu (np. 1 albo 6),
#     → program natychmiast kończy wczytywanie
#     → i liczy statystyki tylko z poprawnych ocen.
#
# PROGRAM MA WYPISAĆ:
#   1) Ile poprawnych ocen wczytano.
#   2) Ile było ocen niedostatecznych (2).
#   3) Ile było "dobrych" ocen: 4 lub 5.
#   4) Średnią arytmetyczną poprawnych ocen.
#
#
# Przykład:
#     Wejście:
#         5
#         3
#         4
#         5
#         1
#
#     Wynik:
#         Wczytano 3 poprawnych ocen
#         Niedostatecznych: 0
#         Dobrych (4 lub 5): 2
#         Średnia: 4.0
#
# ==========================================
ilosc_poprawnych_ocen = 0
liczba_ocen_niedostatecznych = 0
liczba_ocen_dobrych = 0
suma_ocen = 0
ilosc_ocen = int(input("Podaj ilosc ocen: "))

for numer_oceny in range(ilosc_ocen):
    ocena = int(input(f"Podaj ocenę {numer_oceny + 1}: "))
    if ocena < 2 or ocena > 5:
        print("Ocena spoza zakresu! Kończę wczytywanie.")
        break
    ilosc_poprawnych_ocen += 1
    suma_ocen += ocena

    if ocena == 2:
        liczba_ocen_niedostatecznych += 1

    if ocena == 4 or ocena == 5:
        liczba_ocen_dobrych += 1

print(f"Wczytano {ilosc_poprawnych_ocen} poprawnych ocen.")
print(f"Niedostatecznych: {liczba_ocen_niedostatecznych}")
print(f"Dobrych (4 lub 5): {liczba_ocen_dobrych}")
print(f"Średnia: {suma_ocen / ilosc_poprawnych_ocen}")
