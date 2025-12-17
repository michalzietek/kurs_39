def square_function(number):
    return number ** 2

def add_numbers(number_1, number_2):
    return number_1 + number_2

print(square_function(10))
print(square_function(12))

print(add_numbers(1, 2))
print(add_numbers(1, 2000))

# nazwa_funkcji = lambda <parametry do funkcji>: wartość zwracaną z funkcji
square_function_lambda = lambda number: number ** 2

add_numbers_v2 = lambda number_1, number_2: number_1 + number_2

print(add_numbers_v2(10, 12))

print(square_function_lambda(15))