import pprint

# from zajecia_8.lotnisko import Pasazer, LiniaLotnicza, Stewardessa
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
pprint.pprint(lotnisko)