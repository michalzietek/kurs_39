# print("Hello world")
# imie = "Michał"

# print("Witaj w żabce: ")
#
# nazwa_produktu = input("Podaj nazwę produktu, który chcesz kupić: ")
# cena_produktu = float(input("Podaj cenę produktu: "))
#
# if nazwa_produktu == "papierosy" or nazwa_produktu == "piwo" or nazwa_produktu == "energetyk" or nazwa_produktu == "alkohol":
#     wiek = int(input("Podaj swój wiek (jest wymagany): "))
#     if wiek >= 18:
#         print("Mamy ponad 18 lat")
#         print(f"Zakupiłeś {nazwa_produktu} w cenie {cena_produktu}. Masz {wiek} lat.")
#         nazwisko = "Ziętkowski"
#         print(nazwisko)
#     else:
#         print(f"Niestety nie możesz kupić {nazwa_produktu}, Nie masz jeszcze 18 lat.")
# else:
#     print(f"Zakupiłeś {nazwa_produktu} w cenie {cena_produktu}.")
# print("Żegnamy! Do zobaczenia ponownie w żabce!")

"""
if <warunek>: <- warunek musi być prawdziwy
    <kod do wykonania>
else: <- warunek jest fałszywy
    <kod do wykonania>
"""

zawod = input("Podaj zawód w jakim pracujesz: ")
wiek = int(input("Podaj swój wiek: "))

if zawod == "policjant":
    print(f"Do emerytury zostało Ci {50 - wiek} lat.")
elif zawod == "zolnierz":
    print(f"Do emerytury zostało Ci {45 - wiek} lat.")
elif zawod == "nauczyciel":
    print(f"Do emerytury zostało Ci {65 - wiek} lat.")
elif zawod == "programista":
    print(f"Nie dożyjesz emerytury!!!!!")
else:
    print("Niestety nie znam twojego zawodu.")
