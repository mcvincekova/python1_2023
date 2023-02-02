"""
Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
"""

def mult(number_1, number_2):
    result = number_1 * number_2
    return result

# Skratena varianta
def mult_short(a, b):
    return a * b

# Varianta s typovymi anotaciami
def mult_with_types(a: int, b: int) -> int:
    return a * b

# Volanie funkcii

print(mult(10, 14))
print(mult_short(10, 14))
print(mult_with_types(10, 14))



