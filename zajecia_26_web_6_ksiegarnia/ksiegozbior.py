from models import db, Saldo, Book, History


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
    """Zwraca aktualny stan księgarni, w tym saldo, historię i księgozbiór."""
    saldo = Saldo.query.first()
    ksiegozbior = Book.query.all()
    historia = History.query.order_by(History.id).all()
    return {
        "saldo": saldo.value,
        "historia": historia,
        "ksiegozbior": ksiegozbior,
    }

def change_saldo(new_saldo):
    """Zmienia saldo księgarni. Zwraca (True, komunikat) lub (False, błąd)."""
    if new_saldo is None or str(new_saldo).strip() == "":
        return False, "Podaj kwotę zmiany salda."
    try:
        kwota = float(new_saldo)
    except (TypeError, ValueError):
        return False, "Nieprawidłowa kwota. Podaj liczbę."
    saldo = Saldo.query.first()
    saldo.value += kwota
    if saldo.value < 0:
        return False, "Saldo nie może być ujemne."
    db.session.add(saldo)
    db.session.commit()
    return True, f"Saldo zmienione. Aktualne: {saldo.value} zł"


def rent_a_book(numer_isbn):
    """Wypożycza książkę. Zwraca (True, komunikat) lub (False, błąd)."""
    if not numer_isbn or not str(numer_isbn).strip():
        return False, "Wybierz książkę do wypożyczenia."
    ksiegozbior = Book.query.all()
    saldo = Saldo.query.first()
    for ksiazka in ksiegozbior:
        if ksiazka.get("ISBN") == numer_isbn:
            if ksiazka["ilosc_na_stanie"] <= 0:
                return False, f"Książka „{ksiazka['tytul']}” nie jest dostępna (brak na stanie)."
            ksiazka.ilosc_na_stanie -= 1
            saldo.value += 20
            historia_entry = History(details=f"Wypożyczenie książki: {ksiazka['tytul']}, {ksiazka['autor']}, 1 sztuka")
            db.session.add(ksiazka)
            db.session.add(saldo)
            db.session.add(historia_entry)
            db.session.commit()
            return True, f"Wypożyczono: {ksiazka['tytul']}"
    return False, "Nie znaleziono książki o podanym ISBN."


def buy_book(tytul, autor, isbn, rok_wydania, cena, kategoria, ilosc):
    """Zakup książki do księgarni (dostawa). Zwraca (True, komunikat) lub (False, błąd)."""
    saldo = Saldo.query.first()
    ksiegozbior = Book.query.all()
    if not tytul or not str(tytul).strip():
        return False, "Podaj tytuł książki."
    if not autor or not str(autor).strip():
        return False, "Podaj autora."
    if not isbn or not str(isbn).strip():
        return False, "Podaj ISBN."
    try:
        ilosc = int(ilosc)
        cena = float(cena)
        rok_wydania = int(rok_wydania)
    except (TypeError, ValueError):
        return False, "Nieprawidłowe dane: ilość, cena i rok wydania muszą być liczbami."
    if ilosc < 1:
        return False, "Ilość musi być co najmniej 1."
    if cena < 0:
        return False, "Cena nie może być ujemna."
    kwota = cena * ilosc
    if saldo.value - kwota < 0:
        return False, "Niewystarczające saldo. Nie stać księgarni na ten zakup."
    saldo.value -= kwota
    for ksiazka in ksiegozbior:
        if ksiazka.get("ISBN") == isbn:
            ksiazka["ilosc_na_stanie"] += ilosc
            ksiazka["ilosc"] += ilosc
            historia_entry = History(details=f"Uzupełniono stan: „{ksiazka['tytul']}” (+{ilosc} szt.)")
            db.session.add(historia_entry)
            db.session.add(ksiazka)
            db.session.add(saldo)
            db.session.commit()
            return True, f"Uzupełniono stan: „{ksiazka['tytul']}” (+{ilosc} szt.)."

    nowa_ksiazka = Book(
        tytul=tytul.strip(),
        autor=autor.strip(),
        rok=rok_wydania,
        cena=cena,
        kategoria=(kategoria or "").strip() or "inne",
        ilosc_na_stanie=ilosc,
        ilosc=ilosc,
        ISBN=isbn.strip(),
    )
    history_entry = History(details=f"Dodano nową książkę: „{tytul}” ({ilosc} szt.)")
    db.session.add(nowa_ksiazka)
    db.session.add(history_entry)
    db.session.add(saldo)
    db.session.commit()
    return True, f"Dodano do księgozbioru: „{tytul}”."


def show_history(od=None, do=None):
    """Zwraca listę wpisów z historii. od/do – indeksy (int lub None)."""
    historia = History.query.order_by(History.id).all()
    i_od = od if od else 0
    i_do = do if do else len(historia)
    return historia[i_od:i_do]