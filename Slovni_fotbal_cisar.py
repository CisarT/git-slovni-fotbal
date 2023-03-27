#!/usr/bin/env python
# -*- coding: utf-8 -*-

# definice konstant pro barvy
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YEL = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

import random
import string

# funkce pro odstranění diakritiky
def odstran_diakritiku(slovo):
    diakritika = {"á": "a", "č": "c", "ď": "d", "é": "e", "ě": "e",
                  "í": "i", "ň": "n", "ó": "o", "ř": "r", "š": "s",
                  "ť": "t", "ú": "u", "ů": "u", "ý": "y", "ž": "z",
                  "Á": "A", "Č": "C", "Ď": "D", "É": "E", "Ě": "E",
                  "Í": "I", "Ň": "N", "Ó": "O", "Ř": "R", "Š": "S",
                  "Ť": "T", "Ú": "U", "Ů": "U", "Ý": "Y", "Ž": "Z"}
    bez_diakritiky = ""
    for c in slovo:
        if c in diakritika:
            bez_diakritiky += diakritika[c]
        else:
            bez_diakritiky += c
    return bez_diakritiky
# načteně souboru a převod na slova
def nacti_slova(soubor):
    with open(soubor, encoding='utf-8') as f:
        seznam_slov = f.readlines()
    return [odstran_diakritiku(slovo.strip()) for slovo in seznam_slov]
 
# proměná pro načtení seznamu slov ze souboru
seznam_slov = nacti_slova("slovnik_cs_CZ_utf8.txt")

# funkce pro kontrolu, zda je slovo platné
def kontrola_slova(slovo, posledni_pismeno):
    if slovo[0] == posledni_pismeno:
        return True
    else:
        return False

# náhodný výběr slova pro začátek hry
aktualni_slovo = random.choice(seznam_slov)
posledni_pismeno = aktualni_slovo[-1]

print("Hra Slovní fotbal")

# vypíše první slovo jen na začátku hry
print("Startovací náhodné slovo je: ", aktualni_slovo)

# nastaví flag pro první slovo na True
prvni_slovo = True

while True:
    # hráč 1 zadá slovo
    slovo_hrace_1 = input("Hráč 1 zadej slovo (jen malá písmena): ")
    if not slovo_hrace_1:
        print(BLUE + "Chyba: Nezadal jsi žádné slovo." + RESET)
        continue
        
    if kontrola_slova(slovo_hrace_1, posledni_pismeno):
        print(GREEN + "Hráč 1 odpověděl správně!" + RESET)
        posledni_pismeno = slovo_hrace_1[-1]
    else:
        print(YEL + "Hráč 1 odpověděl špatně. Hra končí. Vyhrál hráč 2." + RESET)
        break

    # hráč 2 zadá slovo
    slovo_hrace_2 = input("Hráč 2 zadej slovo (jen malá písmena): ")
    if not slovo_hrace_2:
        print(BLUE + "Chyba: Nezadal jsi žádné slovo." + RESET)
        continue
        
    if kontrola_slova(slovo_hrace_2, posledni_pismeno):
        print(GREEN + "Hráč 2 odpověděl správně!" + RESET)
        posledni_pismeno = slovo_hrace_2[-1]
    else:
        print(RED + "Hráč 2 odpověděl špatně. Hra končí. Vyhrál hráč 1." + RESET)
        break

    # náhodný výběr slova pro další kolo
    aktualni_slovo = random.choice(seznam_slov)
    posledni_pismeno = aktualni_slovo[-1]

    # vypíše další slovo až po prvním kole
    if prvni_slovo:
        prvni_slovo = False
    else:
        print("Další slovo: ", aktualni_slovo)