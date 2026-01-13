def przywitaj_sie():
    print("Hello World")
    return "A to ciekawostka"

# przywitaj_sie()
#
# funkcja = przywitaj_sie
# print(funkcja)
# print("Wykonywanie funkcji: ")
# funkcja()

def zrob_akcje_w_sklepie(nazwa_rzeczy, funkcja_akcji):
    przywitaj_sie()
    print(f"Sprzedajemy: {nazwa_rzeczy}")
    funkcja_akcji()

def sprzedaz_rzeczy():
    print("Sprzedajemy rzecz")

def kupno_rzeczy():
    print("Kupujemy rzecz")

def wymiana_rzeczy():
    print("Wymieniamy rzecz")

# zrob_akcje_w_sklepie("Rower", sprzedaz_rzeczy)
# zrob_akcje_w_sklepie("Rower", kupno_rzeczy)


def dekorator(funkcja):
    def wrapper(*args, **kwargs):
        print("Przed wywołaniem funkcji")
        funkcja(*args, **kwargs)
        print("Po wywołaniu funkcji")
    return wrapper

@dekorator
def powitanie(imie):
    print(f"Cześć, {imie}!")


@dekorator
def zegnaj(imie):
    print(f"Do widzenia, {imie}!")

@dekorator
def przedstaw_sie(imie, nazwisko):
    print(f"Nazywam się {imie} {nazwisko}.")

# powitanie("Michał")
# zegnaj("Anna")
# przedstaw_sie("Krzysztof", "Wiśniewski")


class Pracownik:
    def __init__(self, imie, nazwisko, placa, urlop):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.urlop = urlop

    def __repr__(self):
        return f"Pracownik({self.imie} {self.nazwisko}, Płaca: {self.placa}, Urlop: {self.urlop})"


def sprawdz_czy_zalogowano_administratora(funkcja):
    def wrapper(*args, **kwargs):
        print("Sprawdzanie uprawnień administratora...")
        print("Uprawnienia potwierdzone.")
        funkcja(*args, **kwargs)
        print("Operacja zakończona.")
    return wrapper

class Firma:
    def __init__(self, pracownicy, administratorzy):
        self.pracownicy = pracownicy
        self.administratorzy = administratorzy

    @sprawdz_czy_zalogowano_administratora
    def stworz_urlop(self, pracownik):
        for user in self.pracownicy:
            if user == pracownik:
                print("Tworzenie urlopu dla pracownika...")
                pracownik.urlop = True

    @sprawdz_czy_zalogowano_administratora
    def zmien_place(self, nowa_placa, pracownik):
        for user in self.pracownicy:
            if user == pracownik:
                pracownik.placa = nowa_placa

    @sprawdz_czy_zalogowano_administratora
    def dodaj_pracownika(self, nowy_pracownik):
        self.pracownicy.append(nowy_pracownik)

    @sprawdz_czy_zalogowano_administratora
    def usun_pracownika(self, pracownik_do_usuniecia):
        self.pracownicy.remove(pracownik_do_usuniecia)

    # def sprawdz_administratora(self, nazwa_administratora, rodzaj_operacji, *args):
    #     print("Sprawdzanie uprawnień administratora...")
    #     for admin in self.administratorzy:
    #         if admin == nazwa_administratora:
    #             rodzaj_operacji(*args)
    #             return f"Administrator {nazwa_administratora} wykonał operację: {rodzaj_operacji}"




firma = Firma(pracownicy=[Pracownik("Jan", "Kowalski", 5000, False), Pracownik("Anna", "Nowak", 6000, False)],
              administratorzy=["Admin1", "Admin2"])
firma.usun_pracownika(firma.pracownicy[0])
firma.dodaj_pracownika(Pracownik("Krzysztof", "Wiśniewski", 5500, False))
firma.zmien_place(7000, firma.pracownicy[0])
firma.stworz_urlop(firma.pracownicy[1])
print(firma.pracownicy)
#
# firma.sprawdz_administratora("Admin1", firma.stworz_urlop, firma.pracownicy[0])
# firma.sprawdz_administratora("Admin2", firma.zmien_place, 7000, firma.pracownicy[1])
# firma.sprawdz_administratora("Admin1", firma.dodaj_pracownika, Pracownik("Krzysztof", "Wiśniewski", 5500, False))
# print(firma.pracownicy)