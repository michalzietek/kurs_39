liczba = int(input("Podaj liczbę: "))

if liczba == 0:
    print("Jesteś zerem")
elif liczba < 0:
    print("Jesteś liczbą ujemną")
elif liczba > 0:
    print("Jesteś liczbą dodatnią")
else:
    print("Czym ty w ogóle jesteś?!!")


zawod = input("Podaj swoj zawod: ")

match zawod:
    case "zolnierz":
        print("Jestes zolnierzem!")
    case "policjant":
        print("Jesteś policjantem")
    case "nauczyciel":
        print("Jesteś nauczycielem")
    case "programista":
        print("Jesteś programistą")
    case _:
        print("Nie wiemy jakim zawodem jesteś!")


