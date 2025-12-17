class Student:

    school = "Gimnazjum nr 4"

    def __init__(self, name, surname, class_name):
        self.name = name
        self.surname = surname
        self.class_name = class_name

    def __repr__(self):
        return f"Uczeń {self.name} {self.surname} z klasy: {self.class_name}"

    def change_name(self, new_name):
        self.name = new_name

    @classmethod
    def change_school_name(cls, new_name):
        cls.school = new_name
        pass

    @staticmethod
    def load_data_from_file(file_path):
        with open(file_path) as file:
            return file.read()

student_michal = Student("Michał", "Ziętkowski", "5a")
student_artur = Student("Artur", "Jojko", "1c")

# print(student_artur)
# print(student_michal)
#
# print(id(student_michal.name))
# print(id(student_artur.name))
#
# print(student_michal.school)
# print(student_artur.school)
#
# print(id(student_michal.school))
# print(id(student_artur.school))
# Student.school = "Szkoła podstawowa nr 4"
#
# student_michal.change_school_name("Szkoła specjalna")
# print("po zmianie szkoły dla klasy")
#
# print(student_michal.school)
# print(student_artur.school)
#
# print(id(student_michal.school))
# print(id(student_artur.school))
#
# print("po zmianie szkoły artura")
# student_artur.school = "Szkoła podstawowa nr 9"
#
# print(student_michal.school)
# print(student_artur.school)
#
# print(id(student_michal.school))
# print(id(student_artur.school))
#
#
# student_michal.oceny = [1, 2, 3]
#
# print(student_michal.oceny)

print(id(student_michal.load_data_from_file))
print(id(student_artur.load_data_from_file))

print(id(student_artur.change_school_name))
print(id(student_michal.change_school_name))
