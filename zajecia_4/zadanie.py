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

ilosc_ocen = int(input("Podaj ilosc ocen: "))

for numer_oceny in range(ilosc_ocen):
    ocena = int(input(f"Podaj ocenę {numer_oceny + 1}: "))