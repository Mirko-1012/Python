a = {"  Mela ": 10, "b": 20, "  MELA  ": 30, "c": 40}

b = {}

for chiave, valore in a.items():
    stringa_pulita = chiave.strip().lower()

    if stringa_pulita != "":
        b[stringa_pulita] = valore

lunghezza = len(b)

print(b)
print(lunghezza)