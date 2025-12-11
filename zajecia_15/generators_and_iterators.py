from typing import Iterable, Iterator, Generator

users = [{
        "name": "Bogdan",
        "surname": "Kowalski",
        "email": "bogdan.kowalski@gmail.com"
    },
    {
        "name": "Janusz",
        "surname": "Tracz",
        "email": "cichyzabojca123@gmail.com"
    },
    {
        "name": "Jowita",
        "surname": "Kurek",
        "email": "jowita123@interia.pl"
    }
]

def translate_users_to_new_format(users_list):
    translated_users = []
    for user in users_list:
        new_format = f"{user['name']} {user['surname']} with email address: {user['surname']}"
        translated_users.append(new_format)
    return translated_users

# print(translate_users_to_new_format(users))

def translate_users_to_new_format_generator(users_list):
    for user in users_list:
        new_format = f"{user['name']} {user['surname']} with email address: {user['surname']}"
        yield new_format

# new_format = translate_users_to_new_format_generator(users)
#
# print(new_format)
# print(type(new_format))
# print(isinstance(new_format, Iterable))
# print(isinstance(new_format, Iterator))
#
# for data in new_format:
#     print(data)
#
# for data_2 in new_format:
#     print(f"data_2")

# print(next(new_format))
# print(next(new_format))
# print(next(new_format))
# print(next(new_format))


lista_uczniow = ["Jasiu", "Kasia", "Małgosia"]

# print(isinstance(lista_uczniow, Iterable))
# print(isinstance(lista_uczniow, Iterator))
#
# iterator_uczniow = iter(lista_uczniow)
#
# print(isinstance(iterator_uczniow, Iterator))
#
# print(iterator_uczniow)
#
# for uczen in iterator_uczniow:
#     print(uczen)

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.iterator = iter(self.data.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

my_iterator = MyIterator({"imie": "Michał", "nazwisko": "Ziętkowski", "email": "michalzietkowski@gmail.com"})
#
for data in my_iterator:
    print(data)

#
print(isinstance(my_iterator, Iterator))
print(isinstance(my_iterator, Generator))