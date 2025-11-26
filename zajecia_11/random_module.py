import random

print(random.randint(1, 60))

lista_uczniow = ["Michał", "Józef", "Jan", "Joanna"]

for value in range(100):
    selected_student = random.choices(lista_uczniow, weights=[10000, 10000, 1, 1], k=2)
    print(selected_student)