# Napisz program, który symuluje dodawanie filmów do serwera.
# Każdy film ma podany rozmiar w MB.
#
# Po uruchomieniu programu:
#   1) Program pyta: "Ile filmów chcesz dodać?"
#   2) Następnie wczytuje rozmiar każdego filmu (w MB).
#
# ZASADY:
# - Rozmiar filmu musi być w zakresie od 100 MB do 3000 MB.
# - Jeśli użytkownik poda rozmiar < 100 lub > 3000 MB,
#     → program NATYCHMIAST przerywa wczytywanie
#     → i przechodzi do podsumowania.
#
# - Serwer zapisuje filmy do tzw. SLOTÓW o pojemności 10 000 MB.
# - Filmy dodawane są kolejno:
#       • jeśli kolejny film się mieści — dodaj go
#       • jeśli NIE mieści się — obecny slot zostaje zamknięty,
#         a film trafia do nowego slotu
#
# PODSUMOWANIE, które ma wypisać program:
#   1) Ile slotów utworzono.
#   2) Ile MB łącznie zapisano.
#   3) Ile łącznie było "pustej przestrzeni":
#        pustka = liczba_slotów * 10000 - suma_MB
#   4) Który slot miał najwięcej pustego miejsca oraz ile to było MB.

# DANE WEJŚCIOWE: ilość filmów, rozmiar każdego filmu w MB
# DANE WYJŚCIOWE:
#   1) Ile slotów utworzono.
#   2) Ile MB łącznie zapisano.
#   3) Ile łącznie było "pustej przestrzeni":
#        pustka = liczba_slotów * 10000 - suma_MB
#   4) Który slot miał najwięcej pustego miejsca oraz ile to było MB.

calkowita_wielkosc_filmow = 0
maksymalna_pojemnosc_slotu = 10000
ilosc_slotow = 1
zajete_miejsce_aktualnego_slotu = 0
slot_z_najmniej_zajetym_miejscem = 1
najlzejszy_slot = 10000

ilosc_filmow = int(input("Podaj ilość filmów: "))

for numer_filmu in range(ilosc_filmow):
    rozmiar_filmu = float(input(f"Podaj rozmiar {numer_filmu + 1}(w MB): "))
    if rozmiar_filmu < 10 or rozmiar_filmu > 3000:
        break
    calkowita_wielkosc_filmow += rozmiar_filmu
    if zajete_miejsce_aktualnego_slotu + rozmiar_filmu > maksymalna_pojemnosc_slotu:
        if zajete_miejsce_aktualnego_slotu < najlzejszy_slot:
            najlzejszy_slot = zajete_miejsce_aktualnego_slotu
            slot_z_najmniej_zajetym_miejscem = ilosc_slotow
        ilosc_slotow += 1
        zajete_miejsce_aktualnego_slotu = 0
    zajete_miejsce_aktualnego_slotu += rozmiar_filmu

if zajete_miejsce_aktualnego_slotu < najlzejszy_slot:
    najlzejszy_slot = zajete_miejsce_aktualnego_slotu
    slot_z_najmniej_zajetym_miejscem = ilosc_slotow

if calkowita_wielkosc_filmow == 0:
    ilosc_slotow = 0
    print("Nie dodałeś żadnego filmu!!")
else:
    print(f"Rozmiar wszystkich filmów wynosi: {calkowita_wielkosc_filmow} MB")
    print(f"Ilość wykorzystanych slotów: {ilosc_slotow}")
    print(f"Ilość pustej przestrzeni: {ilosc_slotow * maksymalna_pojemnosc_slotu - calkowita_wielkosc_filmow}")
    print(f"Najlżejszy slot to: {slot_z_najmniej_zajetym_miejscem}, miał {maksymalna_pojemnosc_slotu - najlzejszy_slot} wolnego miejsca.")