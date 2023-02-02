"""
Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.
"""

def print_in_frame(text: str, frame_char: str = '*') -> None:
    """ <dolkumntacia> """

    total_lenght = len(text) + 4

    print(frame_char * total_lenght)
    print(f'{frame_char} {text} {frame_char}')
    print(frame_char * total_lenght)


print_in_frame("A", ".")

