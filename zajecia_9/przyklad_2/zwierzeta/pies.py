class Pies:
    def __init__(self, rasa, wiek, imie):
        self.rasa = rasa
        self.wiek = wiek
        self.imie = imie

    def daj_glos(self):
        print(f"Pies {self.imie} daje głos hau hau!")
