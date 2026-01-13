from abc import ABC, abstractmethod

#Łamiemy zasady liskov + paradygmat programowania obiektowego polimorfizm
# class Pojazd(ABC):
#     def jedz(self):
#         print("Jadę!")
#
#     @abstractmethod
#     def uruchom_silnik(self):
#         pass
#
# class Samochod(Pojazd):
#     def uruchom_silnik(self):
#         return "Uruchamiam silnik spalinowy!"
#
# class Motocykl(Pojazd):
#     def uruchom_silnik(self):
#         return "Uruchamiam silnik w motorze"
#
# class Rower(Pojazd):
#     def uruchom_silnik(self):
#         raise Exception("Niestety rower nie jest w stanie zaimplementować metody uruchom silnik!!")

# class Pojazd(ABC):
#     @abstractmethod
#     def jedz(self):
#         pass
#
# class PojazdSilnikowy(Pojazd):
#     @abstractmethod
#     def uruchom_silnik(self):
#         pass
#
# class PojazdNapedzanySilaMiesni(Pojazd):
#     @abstractmethod
#     def rozgrzej_miesnie(self):
#         pass
#
# class PojazdZSilnikiemElektrycznym(PojazdSilnikowy):
#     @abstractmethod
#     def naladuj_baterie(self):
#         pass
#
#
# class Rower(PojazdNapedzanySilaMiesni):
#
#     def rozgrzej_miesnie(self):
#         pass
#
#     def jedz(self):
#         pass
#
# class Tesla(PojazdZSilnikiemElektrycznym):
#     def naladuj_baterie(self):
#         pass
#
#     def uruchom_silnik(self):
#         pass
#
#     def jedz(self):
#         pass

class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class PaymentWithCard(Payment):
    @abstractmethod
    def get_card_info(self):
        pass


class MastercardPayment(PaymentWithCard):
    def get_card_info(self):
        pass

    def make_payment(self):
        pass

class ClassicWire(Payment):
    def make_payment(self):
        pass