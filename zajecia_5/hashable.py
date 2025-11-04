lista_uczniow = ["Adam", "Ewa", "Tomasz"]
print(id(lista_uczniow))

lista_uczniow.append("Jasiu")
print(id(lista_uczniow))

imie = "Michał"
print(id(imie))
imie += " Ziętkowski"
print(id(imie))

print(hash(imie))
