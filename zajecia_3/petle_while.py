# wiek = int(input("Podaj mi swój wiek: "))
#
# while wiek < 66:
#     if wiek >= 65:
#         print(f"Powinieneś być już na emeryturze. Odpoczywaj po ciężkich latach ;)")
#         break
#     elif wiek == 18:
#         print(f"Masz 18 lat, nie myśl o emeryturze, tylko o pracy ;)")
#         print("Powinieneś korzystać z życia i zrobić sobie imprezę ;)")
#         wiek += 1
#         continue
#     else:
#         print(f"Nie masz jeszcze 65 lat. Twój wiek to: {wiek}")
#         wiek += 1
#     print("Nie masz 18 lat. nie powinieneś robić imprezy osiemnastkowej!!")

"""
while <warunek do spełnienia>: <- tutaj musimy mieć prawdziwy warunek
    <kod do uruchomienia>
"""

liczba = 0
while True:
    liczba += 1
    if liczba == 2:
        pass
    if liczba == 5:
        continue
    print(liczba)
    if liczba == 10:
        break