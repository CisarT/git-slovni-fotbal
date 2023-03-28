import os.path #importovaná knihovna vnitřní(build-in)

#pro instalaci knihovny mimo základ pythonu použiji pip a to příkaz pro instalaci ascii generátoru na převod jpg obrázku na ascii art => pip install ascii_art
#poté pouziji kod :

#from ascii_art import ascii_art

# Načtení obrázku
#image = ascii_art.load_image("sluchátko.jpg")

# Převod obrázku na ASCII art
#asciiObr = ascii_art.convert_image(image)

# Vypsání ASCII artu
#print(asciiObr)

# definice konstant pro barvy
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YEL = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

seznam = {}

# Načtení existujícího seznamu ze souboru (pokud existuje)
if os.path.isfile("telefonni_seznam.py"):
    with open( "telefonni_seznam.py", "r") as f:
        seznam = eval(f.read())

# Funkce pro výpis seznamu
def vypis_seznam():
    print("Seznam kontaktů:")
    for jmeno, cislo in seznam.items():
        print(jmeno + ": " + cislo)

# Funkce pro přidání nového kontaktu
def pridej_kontakt():
    jmeno = input("Zadej jméno: ")
    cislo = input("Zadej telefonní číslo: ")
    # Použití funkce len() pro výpočet délky tel. čísla
    cislo_delka = len(cislo)
    if cislo_delka >= 9:
        seznam[jmeno] = cislo
        with open("telefonni_seznam.py", "w") as f:
            f.write(str(seznam))
        print("Kontakt byl přidán.")
    else:
        print(RED + "Telefoní číslo má málo čísel.Telefoní kontakt nebyl vytvořen!!!!" + RESET,)

# Funkce pro vyhledání kontaktu podle jména
def najdi_kontakt():
    jmeno = input("Zadej jméno kontaktu, kterého chceš najít: ")
    if jmeno in seznam:
        print(jmeno + ": " + seznam[jmeno])
    else:
        print("Kontakt nebyl nalezen.")

# Hlavní cyklus programu
while True:
    print(GREEN + "\nCo chceš udělat?" + RESET)
    print(YEL + " 1 " + RESET + "- Vypsat seznam kontaktů")
    print(YEL + " 2 " + RESET + "- Přidat nový kontakt")
    print(YEL + " 3 " + RESET + "- Najít kontakt")
    print(YEL + " 4 " + RESET + "- Konec programu")

    volba = input(BLUE + "\nZadej číslo volby: " + RESET)

    if volba == "1":
        vypis_seznam()
    elif volba == "2":
        pridej_kontakt()
    elif volba == "3":
        najdi_kontakt()
    elif volba == "4":
        print(GREEN + "\nNaschledanou ........" + RESET)
        break
    else:
        print("Neplatná volba.")
