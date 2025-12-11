class User:
    def __init__(self, name, surname, age, email, list_of_orders):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.orders = list_of_orders

    def __repr__(self):
        return f"Użytkownik {self.name} {self.surname}, ma lat {self.age} i adres email: {self.email}"

    def __int__(self):
        return self.age

    def __bool__(self):
        return len(self.email) > 0

    def __str__(self):
        return f"A sobie przekastowałem obiekt"

    def __setitem__(self, key, value):
        print(f"Key: {key}")
        print(f"Value: {value}")
        if key in self.orders.keys():
            print("Już mamy takie zamówienie")
        else:
            self.orders[key] = value

    def __getitem__(self, item):
        return self.orders.get(item, "Nie masz takiego zamówienia w systemie")

    def hello(self):
        print("Hello world")



user = User("Michał", "Ziętkowski", 30, "michalzietkowski@gmail.com", {})

print(user)

# user.hello()

user_int = int(user)
print(user_int)

print(bool(user))

print(str(user))

user["order_123"] = {"price": 1900, "list_of_items": ["Książka o programowaniu", "Ciepłe skarpetki"]}
user["order_123"] = {"price": 1900, "list_of_items": ["Książka o programowaniu_123", "Ciepłe skarpetki"]}
print(user.orders)

new_order = user["order_456"]
print(new_order)