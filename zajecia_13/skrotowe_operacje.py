### INSTRUKCJA WARUNKOWA

# age = int(input("Podaj mi swój wiek: "))
#
# # is_adult = None
# # if age >= 18:
# #     is_adult = True
# # else:
# #     is_adult = False
#
# is_adult = True if age > 18 else False
#
# # zmienna = <pierwsza wartość> if <warunek do spełnienia dla pierwszej wartości> else <druga wartość>
#
# print(f"Osoba pełnoletnia: {is_adult}")

### LIST COMPREHENSION

students_list = ["Jan", "Kasia", "Basia", "Józef", "Bogdan", "Elżbieta"]
#
# upper_students_list = []
# for student in students_list:
#     upper_students_list.append(student.upper())
#
# print(upper_students_list)
#
# upper_students_comprehension_list = [student.upper() for student in students_list]
#
# print(upper_students_comprehension_list)

# SKŁADNIA:
# nazwa_nowej_struktury (lista) = [<wartosc do dodania w liscie> for <zmienna tymczasowa> in <obiekt iterowalny>]
#
# square_operations = [x**2 for x in range(1000)]
# print(square_operations)

# female_students = []
# for student in students_list:
#     if student.endswith("a"):
#         female_students.append(student)
#
# print(female_students)

female_students = [student for student in students_list if student.endswith("a")]
print(female_students)

# SKŁADNIA:
# nazwa_struktury = [<wartosc do dodania> for <tymczasowa zmienna> in <obiekt iterowalny> if <warunek do spelnienia>]

square_operations_for_numbers_divided_by_two = [x**2 for x in range(20) if x % 2 == 0]

print(square_operations_for_numbers_divided_by_two)
# name = input("Podaj swoje imię: ")
#
# if name.lower() == "kasia":
#     print("jesteś Kasią")

#### DICT COMPREHENSION

users = [
    {
        "imie": "Jan",
        "nazwisko": "Biegański"
    },
    {
        "imie": "Adam",
        "nazwisko": "Nowak"
    },
    {
        "imie": "Anna",
        "nazwisko": "Rogala"
    }
]

users_dict = {index: user for index, user in enumerate(students_list)}

users_comprehension = {user["imie"]: user["nazwisko"] for user in users}

female_users = {user["imie"]: user["nazwisko"] for user in users if user["imie"].endswith("a")}

print(female_users)
print(users_dict)
print(users_comprehension)

# nazwa_slownika = {<klucz>:<wartosc> for <tymczasowa zmienna/zmienne> in <obiekt iterowalny> if <warunek do dodania>}

