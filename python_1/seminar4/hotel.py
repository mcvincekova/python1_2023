"""
Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).
"""
PRICE_NIGHT = 850
PRICE_BREAKFAST = 125


def total_price(persons: int, breakfast: bool = False) -> int:
    """ Calculates total price for staying at the hotel """
    if breakfast:
        price_person = PRICE_NIGHT + PRICE_BREAKFAST
    price_person = PRICE_NIGHT
    
    return persons * price_person

print(total_price(12))