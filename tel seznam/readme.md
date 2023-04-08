Slovní fotbal
Jedná se o konzolovou hru pro dva hráče, kteří se střídají v zadávání slov dle pravidel. Hráč, který jako první nezadá platné slovo, prohrává a druhý hráč vyhrává.

Jak hrát
Stáhněte si soubor se slovníkem slov v češtině slovnik_cs_CZ_utf8.txt a uložte jej do stejného adresáře jako program.

Spusťte program příkazem python slovni_fotbal.py (případně python3 slovni_fotbal.py).

Hráč 1 zadá slovo, které začíná na stejné písmeno, jako končí slovo, které hráč 2 zadal v minulém kole.

Hráč 2 zadá slovo, které začíná na stejné písmeno, jako končí slovo, které hráč 1 zadal.

Hráči se střídají v zadávání slov, dokud jeden z nich nezadá platné slovo.

Pokud hráč 1 nezadá platné slovo, hra končí a hráč 2 vyhrává. Stejně tak, pokud hráč 2 nezadá platné slovo, hra končí a hráč 1 vyhrává.

Po skončení jednoho kola se vygeneruje nové náhodné slovo, na které se začne hrát další kolo.

Pravidla
Slovo musí být v češtině a nesmí obsahovat diakritiku.

Slovo musí začínat na stejné písmeno, jako končí slovo, které předchozí hráč zadal.

Pokud hráč zadá slovo, které nezačíná na správné písmeno, nebo slovo neexistuje, prohrává a hra končí.

Před prvním kolem se vygeneruje náhodné slovo ze seznamu slov, ze kterého se bude hrát.

Hráči se střídají v zadávání slov, dokud jeden z nich nezadá platné slovo.

Jazyk
Program byl napsán v programovacím jazyce Python verze 3.

Verzování
Tento projekt je verzován pomocí systému Git. Pro nejaktuálnější verzi navštivte naši stránku na GitHubu.

Licence
Tento program je poskytován zdarma a bez záruk v rámci licence MIT.