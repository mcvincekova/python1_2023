"""
Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.
"""


numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]

def get_longest_num_size(numbers: list) -> int:
    longest_size = 0

    for num in numbers:
        num_len = len(str(num))
        if num_len > longest_size:
            longest_size = num_len
    
    return longest_size


def indent_output(output_len: int, to_print: str, character: str = '.') -> None:
    num_to_indent = output_len - len(to_print)
    indent = num_to_indent * character
    print(f'{indent}{to_print}')


output_size = get_longest_num_size(numbers)
for number in numbers:
    indent_output(output_size, str(number))