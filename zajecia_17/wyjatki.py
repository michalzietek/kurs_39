# try:
#     age = int(input("Podaj mi swoj wiek: "))
#     print(age)
# except ValueError:
#     print("Niestety musisz podać wartość numeryczną!!")
#
#
# print("Kod po")


lista_uczniow = [
    {
        "imie": "Marek",
        "nazwisko": "Nowak",
        "wiek": 30
    },
    {
        "imie": "Adam",
        "nazwisko": "Małysz",
        "wiek": 45
    }
]

try:
    numer_ucznia = int(input("Podaj numer ucznia: "))
    print(lista_uczniow[numer_ucznia])
except IndexError:
    print("Niestety nie ma takiego numeru!")
except ValueError as e:
    print(f"Numer musi być wartością numeryczną!: {e}")
finally:
    print("To się zawsze wykona!")
