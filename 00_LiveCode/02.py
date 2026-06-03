a = [12, "  Mela ", "Banana", 3.14, "  ArAnCia  ", True, "Kiwi"]

dizionario_stringhe = {}

for elemento in a:
    if type(elemento) == str:
        stringa_sanificata = elemento.strip().lower()
        dizionario_stringhe[stringa_sanificata] = len(stringa_sanificata)

print(dizionario_stringhe)



b = [12, "  Mela ", "Banana", 3.14, "  ArAnCia  ", True, "Kiwi"]

sum = 0

for el in b:
    if type(el) in (int, float):
        sum += el

print(sum)