import math

class FiguraGeometryczna:
    def oblicz_pole(self):
        return 0

    def oblicz_obwod(self):
        return 0

def oblicz_pole_zlozonej_figury(figury: list[FiguraGeometryczna]):
    pole = 0
    for figura in figury:
        pole += figura.oblicz_pole()
    return pole

def oblicz_obwod_zlozonej_figury(figury: list[FiguraGeometryczna]):
    obwod = 0
    for figura in figury:
        obwod += figura.oblicz_obwod()
    return obwod

class Trojkat(FiguraGeometryczna):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return 0.5 * self.podstawa * self.wysokosc

    def oblicz_obwod(self):
        return self.podstawa + 2 * ((self.podstawa / 2) ** 2 + (self.wysokosc ** 2)) ** 0.5

class Prostokat(FiguraGeometryczna):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def oblicz_pole(self):
        return self.bok_a * self.bok_b

    def oblicz_obwod(self):
        return 2* self.bok_a + 2 * self.bok_b

class Kolo(FiguraGeometryczna):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * (self.promien **2)

    def oblicz_obwod(self):
        return 2 * self.promien * math.pi

class Romb(FiguraGeometryczna):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc


lista_figur_1 = [Trojkat(2, 3), Kolo(10), Prostokat(2, 54), Prostokat(5, 5), Romb(100, 20)]

print(oblicz_obwod_zlozonej_figury(lista_figur_1))
print(oblicz_pole_zlozonej_figury(lista_figur_1))

## Złamanie paradygmatu polimorfizmu


# class Zwierze:
#     def plywaj(self):
#         print("Plywam")
#
# class Lew(Zwierze):
#     pass