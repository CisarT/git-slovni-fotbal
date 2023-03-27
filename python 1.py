print("Dotazník")
# Deklarování proměnných
jmeno = input("Zadej jmeno: ")
prijmeni = input("Zadej příjmení: ")
vek = int(input("Zadej věk: "))
cislo_oblibeneho_ctverce = 3

# Vytvoření pole (tuple)
rodne_cislo = input("Zadej rodne číslo: ")

# Vytvoření listu s čísly
cisla = [1, 2, 3, 4, 5]

# Vytvoření slovníku s informacemi o osobě
osoba = {"jmeno": jmeno, "prijmeni": prijmeni, "vek": vek}

# Podmínkový cyklus
if vek >= 18:
  print("Osoba je plnoletá.")
else:
  print("Osoba není plnoletá.")

# For cyklus pro vypsání čísel v listu
for cislo in cisla:
  print(cislo)

# For cyklus pro vypsání informací o osobě ze slovníku
for klic, hodnota in osoba.items():
  print(klic + ": " + str(hodnota))

# Použití funkce len() pro výpočet délky řetězce
delka_jmena = len(jmeno)
print("Počet písmen ve jméně je", delka_jmena)
