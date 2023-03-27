#!/usr/bin/env python
# -*- coding: utf-8 -*-

# definice konstant pro barvy
RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"

import random
import string

words = ['appla']

with open('slovnik_cs_CZ_utf8.txt', 'w') as file:
    for i in range(100):
        word = random.choice(words) + '\n'
        file.write(word)

# funkce pro načtení slov ze souboru
def nacti_slova(soubor):
    with open(soubor, "r") as f:
        seznam_slov = f.readlines()
    return [slovo.strip() for slovo in seznam_slov]
 
# načtení seznamu slov ze souboru
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
        print("Chyba: Nezadal jsi žádné slovo. Zkus to znovu.")
        continue
        
    if kontrola_slova(slovo_hrace_1, posledni_pismeno):
        print(GREEN + "Hráč 1 odpověděl správně!" + RESET)
        posledni_pismeno = slovo_hrace_1[-1]
    else:
        print(RED + "Hráč 1 odpověděl špatně. Hra končí." + RESET)
        break

    # hráč 2 zadá slovo
    slovo_hrace_2 = input("Hráč 2 zadej slovo (jen malá písmena): ")
    if not slovo_hrace_2:
        print("Chyba: Nezadal jsi žádné slovo. Zkus to znovu.")
        continue
        
    if kontrola_slova(slovo_hrace_2, posledni_pismeno):
        print(GREEN + "Hráč 2 odpověděl správně!" + RESET)
        posledni_pismeno = slovo_hrace_2[-1]
    else:
        print(RED + "Hráč 2 odpověděl špatně. Hra končí." + RESET)
        break

    # náhodný výběr slova pro další kolo
    aktualni_slovo = random.choice(seznam_slov)
    posledni_pismeno = aktualni_slovo[-1]

    # vypíše další slovo až po prvním kole
    if prvni_slovo:
        prvni_slovo = False
    else:
        print("Další slovo: ", aktualni_slovo)