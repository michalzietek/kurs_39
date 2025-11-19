"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania numeru ISBN. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne.
"""

from file_handler import file_handler

saldo_ksiegarni = file_handler.saldo
ksiegozbior = file_handler.ksiegozbior
historia = file_handler.historia

while True:
    wybor = input("""
Wybierz jedną z poniższych komend:
1. doładowanie
2. wypożycz
3. zakup
4. bieżący_stan
5. zestawienie
6. szczegóły_książki
7. dziennik
8. zakończ
Podaj numer komendy: """)

    match wybor:
        case "1":
            srodki = float(
                input("Podaj kwotę do doładowania (lub ujemną do odjęcia): ")
            )
            if saldo_ksiegarni + srodki < 0:
                print("Nie możesz ustawić salda na wartość ujemną.")
            else:
                saldo_ksiegarni += srodki
                print(f"Aktualne saldo: {saldo_ksiegarni:.2f} PLN")
                historia.append(f"Zmiana salda o {srodki} PLN")
        case "2":
            numer_isbn = input("Podaj numer ISBN książki do wypożyczenia: ")
            znaleziono_ksiazke = False
            for ksiazka in ksiegozbior:
                if ksiazka.get("ISBN") == numer_isbn:
                    znaleziono_ksiazke = True
                    if ksiazka["ilosc_na_stanie"] <= 0:
                        print("Nie ma tej książki na stanie.")
                        break
                    ksiazka["ilosc_na_stanie"] -= 1
                    saldo_ksiegarni += 20  # koszt wypożyczenia książ
            if not znaleziono_ksiazke:
                print("Nie znaleziono książki o podanym numerze ISBN.")
        case "3":
            tytul = input("Podaj tytuł książki: ")
            autor = input("Podaj autora książki: ")
            koszt = float(input("Podaj koszt zakupu książki: "))
            ilosc = int(input("Podaj ilość egzemplarzy: "))
            kategoria = input("Podaj kategorię książki: ")
            numer_isbn = input("Podaj numer ISBN książki: ")
            rok_wydania = int(input("Podaj rok wydania książki: "))
            if saldo_ksiegarni - (koszt * ilosc) < 0:
                print("Nie możesz ustawić salda na wartość ujemną.")
                continue
            else:
                saldo_ksiegarni -= koszt * ilosc
            ksiegozbior.append(
                {
                    "autor": autor,
                    "tytul": tytul,
                    "rok_wydania": rok_wydania,
                    "cena": koszt,
                    "ilosc_na_stanie": ilosc,
                    "kategoria": kategoria,
                    "ilosc": ilosc,
                    "ISBN": numer_isbn,
                }
            )
        case "4":
            print(f"Aktualne saldo: {saldo_ksiegarni} PLN")
        case "5":
            print("Zestawienie księgozbioru:")
            print(ksiegozbior)
        case "6":
            numer_isbn = input("Podaj numer ISBN książki: ")
            znaleziono_ksiazke = False
            for ksiazka in ksiegozbior:
                if ksiazka.get("ISBN") == numer_isbn:
                    znaleziono_ksiazke = True
                    print(f"Szczegóły książki: {ksiazka}")
                    break
            if not znaleziono_ksiazke:
                print("Nie znaleziono książki o podanym numerze ISBN.")
        case "7":
            od = input(
                "Podaj wartość 'od' (numer transakcji), jeśli nie chcesz nic nie podawaj: "
            )
            do = input(
                "Podaj wartość 'do' (numer transakcji), jeśli nie chcesz nic nie podawaj: "
            )
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(historia)
            print(f"Dziennik transakcji:{historia[od:do]}")
        case "8":
            print("Koniec działania programu.")
            break

file_handler.save_data_to_file(new_saldo=saldo_ksiegarni, new_historia=historia, new_ksiegozbior=ksiegozbior)