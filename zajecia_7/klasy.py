# auta = [{
#         "marka": "Audi",
#         "model": "a1",
#         "moc": 150,
#         "przebieg": 99000,
#         "wlaczone": False
#     },
#     {
#         "marka": "Opel",
#         "model": "astra",
#         "moc": 120,
#         "przebieg": 180000,
#         "wlaczone": False
#     }
# ]
#
# def wlacz_silnik(auto):
#     if auto.get("wlaczone"):
#         print("Silnik już włączony")
#     else:
#         auto["wlaczone"] = True
#
# marka_auta = input("Podaj markę auta: ")
#
# for auto in auta:
#     if auto.get("marka") == marka_auta:
#         wlacz_silnik(auto)


class Auto:
    def __init__(self, marka, model, moc, przebieg, wlaczone):
        self.marka = marka
        self.model = model
        self.moc = moc
        self.przebieg = przebieg
        self.silnik_wlaczony = wlaczone

    def __str__(self):
        return f"Auto {self.marka}, {self.model}, o mocy {self.moc} KM, przebiegu {self.przebieg}. Silnik jest włączony? {self.silnik_wlaczony}"

    def wlacz_silnik(self):
        if self.silnik_wlaczony:
            print("Silnik jest już włączony")
        else:
            self.silnik_wlaczony = True
            print("Włączamy silnik")


audi = Auto(marka="Audi", model="A5", moc=299, przebieg=40000, wlaczone=False)

audi.wlacz_silnik()
print(audi)
