# import operacje_matematyczne
from operacje_matematyczne import dodawanie, odejmowanie
# from zajecia_9.przyklad_1.operacje_matematyczne import dodawanie, odejmowanie
from pies import burek as pies_rasowy

def witaj(imie="Adam"):
    print(f"Witaj {imie}")

witaj("Michał")

witaj()

# print(operacje_matematyczne.dodawanie(1, 2))
# print(operacje_matematyczne.odejmowanie(5, 4))

pies_rasowy.daj_glos()

print(dodawanie(1, 2))
print(odejmowanie(7, 2))