"""
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
"""

from monitoring import monitor

class Pasazer:
    def __init__(self, imie, nazwisko, numer_lotu, numer_miejsca_w_samolocie=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu
        self.numer_miejsca_w_samolocie = numer_miejsca_w_samolocie

    def __repr__(self):
        return f"Pasażer {self.imie} {self.nazwisko} z lotu {self.numer_lotu} i miejscu {self.numer_miejsca_w_samolocie}"


class LiniaLotnicza:
    def __init__(self, nazwa_linii, lista_lotow):
        self.nazwa = nazwa_linii
        self.lista_lotow = lista_lotow

    def __repr__(self):
        return f"Linia lotnicza {self.nazwa} z lotami: {self.lista_lotow}"


class Stewardessa:
    def __init__(self, imie, nazwisko, numer_lotu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_lotu = numer_lotu

    def __repr__(self):
        return (
            f"Stewardessa {self.imie} {self.nazwisko} obsługująca lot {self.numer_lotu}"
        )


#
# lotnisko = [
#     ,
#
# ]

lotnisko = {
    "pasazerowie": [
        Pasazer("Jan", "Kowalski", "LO123"),
        Pasazer("Kamila", "Nowak", "EMI123"),
        Pasazer("Janusz", "Bolec", "LO123"),
    ],
    "linie_lotnicze": [
        LiniaLotnicza("LOT", ["LO123", "LO345"]),
        LiniaLotnicza("Emirates", ["EMI123", "EMI555"]),
    ],
    "stewardessy": [Stewardessa("Jadwiga", "Kloszard", "LO123")],
}

@monitor
def wyszukaj_pasazerow_lotu(pasazerowie, numer_lotu):
    pasazerowie_lotu = []
    for pasazer in pasazerowie:
        if pasazer.numer_lotu == numer_lotu:
            pasazerowie_lotu.append(pasazer)
    return pasazerowie_lotu


@monitor
def wyszukaj_linie_lotnicza_pasazera(imie, nazwisko, lotnisko):
    numer_lotu_pasazera = None
    int("abddd")
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            numer_lotu_pasazera = int(pasazer.numer_lotu)
    if numer_lotu_pasazera:
        for linia in lotnisko.get("linie_lotnicze"):
            if numer_lotu_pasazera in linia.lista_lotow:
                return linia.nazwa

@monitor
def znajdz_loty_linii_lotniczej(nazwa_linii, linie):
    for linia in linie:
        if linia.nazwa == nazwa_linii:
            return linia.lista_lotow

@monitor
def znajdz_lot_stewardessy(imie, nazwisko, lista_stewardess):
    for stewardessa in lista_stewardess:
        if stewardessa.imie == imie and stewardessa.nazwisko == nazwisko:
            return stewardessa.numer_lotu


while True:
    wybor_uzytkownika = input("Wybierz opcję:\n1. Dodaj\n2. Zarządzaj\n3. Zakończ\n")
    if wybor_uzytkownika == "1":
        obiekt_do_dodania = input(
            "Co chcesz dodać?\n1. Pasażer\n2. Linia lotnicza\n3. Stewardessa"
        )
        match obiekt_do_dodania:
            case "1":
                imie_pasazera = input("Podaj imię pasażera: ")
                nazwisko_pasazera = input("Podaj nazwisko pasażera: ")
                numer_lotu_pasazera = input("Podaj numer lotu pasażera: ")
                miejsce_pasazera = input("Podaj miejsce pasażera w samolocie: ")
                pasazer = Pasazer(
                    imie_pasazera,
                    nazwisko_pasazera,
                    numer_lotu_pasazera,
                    miejsce_pasazera,
                )
                lotnisko["pasazerowie"].append(pasazer)
            case "2":
                nazwa_linii = input("Podaj nazwę linii: ")
                lista_lotow = []
                while True:
                    lot = input("Podaj lot linii(aby zakończyć kliknij enter): ")
                    if not lot:
                        break
                    else:
                        lista_lotow.append(lot)
                linia = LiniaLotnicza(nazwa_linii=nazwa_linii, lista_lotow=lista_lotow)
                lotnisko["linie_lotnicze"].append(linia)
            case "3":
                imie = input("Podaj imię stewardessy: ")
                nazwisko = input("Podaj nazwisko stewardessy: ")
                numer_lotu = input("Podaj numer lotu stewardessy: ")
                lotnisko["stewardessy"].append(
                    Stewardessa(imie=imie, nazwisko=nazwisko, numer_lotu=numer_lotu)
                )
    elif wybor_uzytkownika == "2":
        opcja_do_edycji = input(
            "Czym chcesz zarządzać?\n1. Lot\n2. Pasażer\n3. Linia lotnicza\n4. Stewardessa\n"
        )
        match opcja_do_edycji:
            case "1":
                numer_lotu = input(
                    "Podaj numer lotu, dla którego chcesz znaleźć pasażerów: "
                )
                pasazerowie_lotu = wyszukaj_pasazerow_lotu(
                    lotnisko.get("pasazerowie"), numer_lotu
                )
                print(f"Pasażerowie lotu to: {pasazerowie_lotu}")
            case "2":
                imie_pasazera = input("Podaj imię pasażera: ")
                nazwisko_pasazera = input("Podaj nazwisko pasażera: ")
                linia = wyszukaj_linie_lotnicza_pasazera(
                    imie=imie_pasazera, nazwisko=nazwisko_pasazera, lotnisko=lotnisko
                )
                if linia:
                    print(f"Nazwa linii {imie_pasazera} {nazwisko_pasazera} to {linia}")
                else:
                    print(
                        "Nie ma takiego pasażera lub nie mamy takiej linii lotniczej."
                    )
            case "3":
                nazwa_linii = input("Podaj nazwę linii lotniczej: ")
                lista_lotow = znajdz_loty_linii_lotniczej(
                    nazwa_linii, lotnisko.get("linie_lotnicze")
                )
                print(f"Lista lotów {nazwa_linii} to {lista_lotow}")
            case "4":
                imie = input("Podaj imię stewardessy: ")
                nazwisko = input("Podaj nazwisko stewardessy: ")
                numer_lotu_stewardessy = znajdz_lot_stewardessy(
                    imie, nazwisko, lotnisko.get("stewardessy")
                )
                lista_pasazerow = wyszukaj_pasazerow_lotu(
                    lotnisko.get("pasazerowie"), numer_lotu_stewardessy
                )
                print(
                    f"Pasażerowie lotu stewardessy {imie} {nazwisko} to {lista_pasazerow}"
                )
    elif wybor_uzytkownika == "3":
        break
