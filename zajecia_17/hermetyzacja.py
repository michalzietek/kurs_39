class KontoBankowe:
    def __init__(self, numer_konta, saldo, karta):
        self.numer_konta = numer_konta
        self._saldo = saldo
        self.__karta = karta

    def set_saldo(self, new_saldo):
        print("Informujemy klienta o zmianie salda!!")
        self._saldo = new_saldo

    def get_karta(self):
        print(self.__karta)

    @property
    def karta(self):
        return self.__karta

    @property
    def saldo(self):
        return self._saldo

konto_michala = KontoBankowe("1234352435", 100, "Mastercard 21343452425 25243 5 245")

konto_michala.numer_konta = "5454454"
konto_michala._saldo = 100000000

print(konto_michala._saldo)
konto_michala.get_karta()
print(konto_michala._KontoBankowe__karta)