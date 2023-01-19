tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

ticket_number = int(input("Zadaj cislo listku: "))

if ticket_number in tombola:
    winnings = tombola.pop(ticket_number)
    print(f"Gratujem vyhravas {winnings}")
else:
    print("Smola")