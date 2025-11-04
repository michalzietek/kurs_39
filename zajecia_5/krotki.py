uczniowie = ("Andrzej", "Ela", "Michał")
krotka_ciekawa = (True, 1.0, "Adam", None)

krotka_3 = tuple(("Adam", "Ewa"))

krotka_4 = "Adam", "Ewa"
imie = "Michal",
# print(uczniowie)
# print(krotka_ciekawa)
# print(krotka_3)
# print(type(uczniowie))
print(type(krotka_4))
print(krotka_4)
print(imie)
print(type(imie))
print(uczniowie[0])
for uczen in uczniowie:
    print(uczen)


print(id(krotka_4))
krotka_4 = "Jan", "Adam"
print(id(krotka_4))
print(krotka_4)