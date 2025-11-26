import datetime

def add_numbers(first_number, second_number):
    return first_number + second_number



user = {
    "name": "Michał",
    "surname":  "Ziętkowski",
    "gross_salary": 3500,
    "age": 30,
}
def calculate_net_salary(user: dict) -> dict:
    salaries_netto = {}
    if user.get("gross_salary") * 12 > 120000:
        tax_rate = 0.32
    else:
        tax_rate = 0.12

    for month in range(1, 13):
        gross_salary = user.get("gross_salary", 0)
        tax = gross_salary * tax_rate
        net_salary = gross_salary - tax
        salaries_netto[f"month_{month}"] = net_salary

    return salaries_netto


print(calculate_net_salary(user))


