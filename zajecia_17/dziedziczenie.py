class Vehicle:
    def __init__(self, type, mark):
        self.type = type
        self.mark = mark

    def move(self):
        print("Starting to move")

    def make_a_honk(self):
        print("Beep beep")

    def cleanup(self):
        print("Cleaning up a vehicle!")

class PreExhibit:
    def cleanup(self):
        print("Cleaning up prexhibit")

class Exhibit(PreExhibit):
    def renovate(self):
        print("renovating an exhibit!!")


class Car(Exhibit, Vehicle):
    def __init__(self, mark, model, type):
        self.mark = mark
        self.model = model
        self.type = type

    def start_engine(self):
        print("Startuję silnik")


class Tank(Vehicle, Exhibit):
    def __init__(self, mark, type_of_armat):
        self.mark = mark
        self.type_of_armat = type_of_armat

    def start_shooting(self):
        print("Zaczynam szczelać!")

    def make_a_honk(self):
        print("I am not gonna honk!")

car_1 = Car("Audi", "A5", "cabrio")

car_1.start_engine()

car_1.move()
car_1.make_a_honk()

tank = Tank("leopard", "big")

tank.make_a_honk()

car_1.renovate()
tank.renovate()

car_1.cleanup()

print(dir(car_1))