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

seznam = {}

# Načtení existujícího seznamu ze souboru (pokud existuje)
if os.path.isfile("telefonni_seznam.py"):
    with open("telefonni_seznam.py", "r") as f:
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
        print("Telefoní číslo má málo čísel")

# Funkce pro vyhledání kontaktu podle jména
def najdi_kontakt():
    jmeno = input("Zadej jméno kontaktu, kterého chceš najít: ")
    if jmeno in seznam:
        print(jmeno + ": " + seznam[jmeno])
    else:
        print("Kontakt nebyl nalezen.")

# Hlavní cyklus programu
while True:
    print("\nCo chceš udělat?")
    print("1 - Vypsat seznam kontaktů")
    print("2 - Přidat nový kontakt")
    print("3 - Najít kontakt")
    print("4 - Konec programu")

    volba = input("Zadej číslo volby: ")

    if volba == "1":
        vypis_seznam()
    elif volba == "2":
        pridej_kontakt()
    elif volba == "3":
        najdi_kontakt()
    elif volba == "4":
        break
    else:
        print("Neplatná volba.")
