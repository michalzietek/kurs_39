# plik = open("kamikaze.txt")
# # plik.read()
# # print(plik.readline())
# # for linijka in plik:
# #     print(linijka)
#
# tekst = plik.readlines()
# # print(tekst)
# # teskt_2 = []
# # for linijka in tekst:
# #     teskt2_2.append(linijka.replace("\n", ""))
# # print(teskt_2)
# # print("Przed zamykaniem pliku!")
# plik.close()
#
# with open("kamikaze.txt") as plik:
#     print(plik.readlines())
#
# class WirtualnyAsystent:
#     def __enter__(self):
#         print("Przygotowuję agendę spotkania")
#         print("Parzę kawę dla gości")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Sprzątam po spotkaniu")
#         print("Zbieram informację, notatki i action pointy ze spotkania")
#
#
# with WirtualnyAsystent() as asystent:
#     print("Omawiamy szczegóły kampanii reklamowej")

# with open("kamikaze.txt", mode="r") as plik:
#     # plik.write("To jest mój freestyle łaka maka fą!")
#     print(plik.read())

# with open("kamikaze.txt", mode="w") as plik:
#     plik.write("To jest mój freestyle łaka maka fą!")

# with open("kamikaze.txt", mode="a") as plik:
#     print(plik.read())
#     plik.write("To jest mój freestyle łaka maka fą!")

with open("kamikaze4.txt", "r+") as plik:
    print(plik.read())
    plik.write("To jest mój freestyle łaka maka fą!")

with open("kamikaze3.txt", "w+") as plik:
    print(plik.read())
    plik.write("aaaaaaaaaa")
    plik.write("aaaaaaaaaa")

with open("kamikaze2.txt", "a+") as plik:
    plik.write("nowa piosenka")
