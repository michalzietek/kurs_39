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

class Pojazd(ABC):
    @abstractmethod
    def jedz(self):
        pass

class Silnikowe(ABC):
    @abstractmethod
    def uruchom_silnik(self):
        pass

class NapedzaneSilaMiesni(ABC):
    @abstractmethod
    def rozgrzej_miesnie(self):
        pass

class Elektryczne(ABC):
    @abstractmethod
    def naladuj_baterie(self):
        pass

class Rower(Pojazd, NapedzaneSilaMiesni):
    def jedz(self):
        pass

    def rozgrzej_miesnie(self):
        pass