import math
from abc import ABC, abstractmethod

class FiguraGeometryczna(ABC):

    @abstractmethod
    def oblicz_pole(self):
        return 0

    @abstractmethod
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
    def oblicz_pole(self):
        pass

    def oblicz_obwod(self):
        pass

    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc


lista_figur_1 = [Trojkat(2, 3), Kolo(10), Prostokat(2, 54), Prostokat(5, 5), Romb(100, 20)]

print(oblicz_obwod_zlozonej_figury(lista_figur_1))
print(oblicz_pole_zlozonej_figury(lista_figur_1))


class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass

class PayUPayment(Payment):
    def process_payment(self):
        print(f"Przechodzimy na stronę payu i tam kończymy płatność")

class BlikPayment(Payment):
    def process_payment(self):
        pass

    def generate_code(self):
        print("Generuję kod")

class Order:
    def __init__(self, items, carrier, payment_method, address):
        self.items = items
        self.carrier = carrier
        self.payment_method = payment_method
        self.address = address

    def proess_order(self):
        self.payment_method.process_payment()
        self.items.remove_quantity()
        self.carrier.create_shipment()
