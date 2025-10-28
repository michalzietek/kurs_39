from collections.abc import Iterable

# print(isinstance(5, Iterable))
# print(isinstance(range(5), Iterable))

# ilosc_ocen = int(input("Podaj ilość ocen do średniej: "))
# suma_ocen = 0

# obecna_ocena = 0
#
# while obecna_ocena < ilosc_ocen:
#     obecna_ocena += 1
#     ocena = int(input("Podaj ocenę: "))
#     suma_ocen += ocena
# print(f"Srednia arytmetyczna z ocen to: {suma_ocen/ilosc_ocen}")

# for ocena_lp in range(ilosc_ocen):
#     ocena = int(input("Podaj ocenę: "))
#     suma_ocen += ocena
#
# print(f"Srednia arytmetyczna z ocen to: {suma_ocen/ilosc_ocen}")


for litera in "michal":
    if litera == "c":
        break
    print(f"litera: {litera}")

print(litera)
"""
for <tymczasowa_zmienna> in <obiekt, po którym będziemy iterować>:
    <blok kodu>
"""