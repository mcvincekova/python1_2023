# importujte modul sys 
# Dokumentacia: (https://docs.python.org/3/library/sys.html)
import sys


print("Vitejte u nas v divadle!") 
nazev_hry = "Romeo a Julie"
cena_listku = 150

# Nacitaj vek od uzivatela a uloz ho ako cislo (int) do premennej vek
vek = int(input("Zadaj vek: "))

# V pripade, ze vek je menej ako 13 rokov, ukonci program pomocou prikazu exit()
# Dokumentacia: https://docs.python.org/3/library/sys.html#sys.exit
if vek <= 13:
    sys.exit("Vek musi byt aspon 13.")

# Nacitaj pocet listkov od uzivatela a uloz ho ako cislo (int) do premennej pocet_listku
pocet_listku = int(input("Zadejte prosim pocet listku: "))

# Ak je pocet listkov aspon 3, zakaznik dostane jeden zdarma
if pocet_listku >= 3:
    print("Pri nakupe aspon troch listkov ostavate 1 listok zdarma!")
    # zaplat o jeden listok menej ako je pocet listkov
    celkova_cena = (pocet_listku - 1) * cena_listku
else:
    celkova_cena = pocet_listku * cena_listku

print(f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}.")
