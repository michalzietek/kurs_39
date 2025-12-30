class Silnik:
    def __init__(self, pojemnosc, moc):
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.wlaczony = False

    def wlacz_silnik(self):
        print("Włączam silnik")
        self.wlaczony = True

    def wymien_olej(self):
        print(f"Wymieniam olej w silniku {self.pojemnosc} o mocy {self.moc}")


class Zawieszenie:
    def __init__(self, typ_zawieszenia):
        self.typ_zawieszenia = typ_zawieszenia

    def wymien_czesci_reuzywalne(self):
        print("Wymieniam części")


class UkladNapedowy:
    def __init__(self, uklad_napedowy):
        self.uklad_napedowy = uklad_napedowy


class Samochod:
    def __init__(self, model, marka, silnik, zawieszenie, uklad_napedowy):
        self.model = model
        self.marka = marka
        self.silnik = silnik
        self.zawieszenie = zawieszenie
        self.uklad_napedowy = uklad_napedowy

    def uruchom_auto(self):
        print(f"Uruchamiam auto {self.marka} {self.model}")
        self.silnik.wlacz_silnik()

    def serwisuj_auto(self):
        self.silnik.wymien_olej()
        self.zawieszenie.wymien_czesci_reuzywalne()

silnik_1_5 = Silnik("1500", 150)
silnik_2_0 = Silnik("2000", 190)

zawieszenie_sportowe = Zawieszenie("sportowe")
zawieszenie_terenowe = Zawieszenie("terenowe")

uklad_napedowy_przedni = UkladNapedowy("na przednia os")
uklad_napedowy_tylni = UkladNapedowy("na tynia os")
uklad_napedowy_4x4 = UkladNapedowy("4x4")

samochod_sportowy = Samochod("Porsche", "911", silnik_2_0, zawieszenie_sportowe, uklad_napedowy_przedni)
samochod_terernowy = Samochod("Jeep", "Cheeroke", silnik_1_5, zawieszenie_terenowe, uklad_napedowy_4x4)

samochod_terernowy.uruchom_auto()
samochod_sportowy.uruchom_auto()

samochod_sportowy.serwisuj_auto()
samochod_terernowy.serwisuj_auto()