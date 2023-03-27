# Deklarování proměnných
jmeno = "Jan"
prijmeni = "Novák"
vek = 25
cislo_oblibeneho_ctverce = 3

# Vytvoření pole (tuple)
rodne_cislo = (850101/1234, 900301/5678, 920201/4321)

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
,