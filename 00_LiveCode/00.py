a = ["a", "b", "C", "d", "e"]

b = []

for el in a:
    stringa_pulita = el.strip().lower()

    if stringa_pulita != "" and stringa_pulita not in b:
        b.append(stringa_pulita)

lunghezza = len(b)

print(b)
print(lunghezza)
