def przywitaj_sie(imie):
    return f"Cześć, {imie}!"

print(przywitaj_sie("Michał"))

def przywitaj_sie_2(*args):
    print(args)
    print(type(args))
    return f"Cześć {args}"

print(przywitaj_sie_2("Michał", "Anna", "Krzysztof", 123, True, [1, 2, 3]))
przywitaj_sie_2()

def przywitaj_sie_3(**kwargs):
    print(kwargs)
    print(type(kwargs))

przywitaj_sie_3(imie_1="Michał", imie_2="Anna", imie_3="Krzysztof")



def funkcja_sprawdzajaca_zalogowanie():
    print("Sprawdzam czy zalogowano administratora")
    print("Logujemy administratora")

def wyloguj_administratora():
    print("Wylogowujemy administratora")

def zrob_przelew(amount, recipient):
    funkcja_sprawdzajaca_zalogowanie()
    print(f"Robimy przelew {amount} PLN do {recipient}")
    return amount
    wyloguj_administratora()