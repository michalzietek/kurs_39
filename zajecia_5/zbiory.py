kolory = {"czerwony", "czarny", "niebieski"}
zbior = {True, "Adam", 2.0, "zielony"}
print(kolory)
for kolor in kolory:
    print(kolor)

print("czerwony" in kolory)

kolory.add("zielony")
print(kolory)
kolory.remove("czerwony")
print(kolory)

test_zbior = {True, [1, 2, 3]}
print(test_zbior)


kolory.add("zielony")
print(kolory)