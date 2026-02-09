from file_handler import file_handler


# while True:
#     wybor = input("""
# Wybierz jedną z poniższych komend:
# 1. doładowanie
# 2. wypożycz
# 3. zakup
# 4. bieżący_stan
# 5. zestawienie
# 6. szczegóły_książki
# 7. dziennik
# 8. zakończ
# Podaj numer komendy: """)
#
#     match wybor:
#         case "1":
#             srodki = float(
#                 input("Podaj kwotę do doładowania (lub ujemną do odjęcia): ")
#             )
#             if saldo_ksiegarni + srodki < 0:
#                 print("Nie możesz ustawić salda na wartość ujemną.")
#             else:
#                 saldo_ksiegarni += srodki
#                 print(f"Aktualne saldo: {saldo_ksiegarni:.2f} PLN")
#                 historia.append(f"Zmiana salda o {srodki} PLN")
#         case "2":
#             numer_isbn = input("Podaj numer ISBN książki do wypożyczenia: ")
#             znaleziono_ksiazke = False
#             for ksiazka in ksiegozbior:
#                 if ksiazka.get("ISBN") == numer_isbn:
#                     znaleziono_ksiazke = True
#                     if ksiazka["ilosc_na_stanie"] <= 0:
#                         print("Nie ma tej książki na stanie.")
#                         break
#                     ksiazka["ilosc_na_stanie"] -= 1
#                     saldo_ksiegarni += 20  # koszt wypożyczenia książ
#             if not znaleziono_ksiazke:
#                 print("Nie znaleziono książki o podanym numerze ISBN.")
#         case "3":
#             tytul = input("Podaj tytuł książki: ")
#             autor = input("Podaj autora książki: ")
#             koszt = float(input("Podaj koszt zakupu książki: "))
#             ilosc = int(input("Podaj ilość egzemplarzy: "))
#             kategoria = input("Podaj kategorię książki: ")
#             numer_isbn = input("Podaj numer ISBN książki: ")
#             rok_wydania = int(input("Podaj rok wydania książki: "))
#             if saldo_ksiegarni - (koszt * ilosc) < 0:
#                 print("Nie możesz ustawić salda na wartość ujemną.")
#                 continue
#             else:
#                 saldo_ksiegarni -= koszt * ilosc
#             ksiegozbior.append(
#                 {
#                     "autor": autor,
#                     "tytul": tytul,
#                     "rok_wydania": rok_wydania,
#                     "cena": koszt,
#                     "ilosc_na_stanie": ilosc,
#                     "kategoria": kategoria,
#                     "ilosc": ilosc,
#                     "ISBN": numer_isbn,
#                 }
#             )
#         case "4":
#             print(f"Aktualne saldo: {saldo_ksiegarni} PLN")
#         case "5":
#             print("Zestawienie księgozbioru:")
#             print(ksiegozbior)
#         case "6":
#             numer_isbn = input("Podaj numer ISBN książki: ")
#             znaleziono_ksiazke = False
#             for ksiazka in ksiegozbior:
#                 if ksiazka.get("ISBN") == numer_isbn:
#                     znaleziono_ksiazke = True
#                     print(f"Szczegóły książki: {ksiazka}")
#                     break
#             if not znaleziono_ksiazke:
#                 print("Nie znaleziono książki o podanym numerze ISBN.")
#         case "7":
#             od = input(
#                 "Podaj wartość 'od' (numer transakcji), jeśli nie chcesz nic nie podawaj: "
#             )
#             do = input(
#                 "Podaj wartość 'do' (numer transakcji), jeśli nie chcesz nic nie podawaj: "
#             )
#             if od:
#                 od = int(od)
#             else:
#                 od = 0
#             if do:
#                 do = int(do)
#             else:
#                 do = len(historia)
#             print(f"Dziennik transakcji:{historia[od:do]}")
#         case "8":
#             print("Koniec działania programu.")
#             break

# file_handler.save_data_to_file(new_saldo=saldo_ksiegarni, new_historia=historia, new_ksiegozbior=ksiegozbior)

def get_bookstore_state():
    """Returns the current state of the bookstore."""
    return {
        "saldo": file_handler.saldo,
        "ksiegozbior": file_handler.ksiegozbior,
        "historia": file_handler.historia,
    }

def change_saldo(new_saldo):
    """Changes the bookstore's balance."""
    file_handler.saldo = float(new_saldo)
    file_handler.save_data_to_file(
        new_saldo=file_handler.saldo,
        new_historia=file_handler.historia,
        new_ksiegozbior=file_handler.ksiegozbior,
    )

def rent_a_book(numer_isbn):
    for ksiazka in file_handler.ksiegozbior:
        if ksiazka.get("ISBN") == numer_isbn:
            ksiazka["ilosc_na_stanie"] -= 1
            file_handler.saldo += 20  # koszt wypożyczenia książki
            file_handler.historia.append(
                f"Wypożyczono książkę o ISBN {numer_isbn}"
            )
            file_handler.save_data_to_file(
                new_saldo=file_handler.saldo,
                new_historia=file_handler.historia,
                new_ksiegozbior=file_handler.ksiegozbior,
            )
            return f"Wypożyczono książkę: {ksiazka['tytul']}"