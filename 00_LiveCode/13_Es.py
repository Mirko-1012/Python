a = ["gm", 27, "u"]

print(a[0], a[1], a[2]) #Indice numerico ordinato

d = {'key': 'value', 'nome':'Gianmarco', 'age':27, 'gender': 'Uomo'} # Dizionario

print(type(d))
print(d)

print(f"Nome: {d['nome']}")
print(f"Genere: {d['gender']}")
print(f"Età: {d['age']}")

print(d.get('titolodistudio', 'Chiave non esistente')) # cosa fa se non trova la chiave

b = input("Dimmi cosa vuoi sapere di questo tipo: ")
print(d.get(b, 'chiave non esistente'))

if 'tifo' in d:
    print(d['tifo'])
else:
    print("niente da printare")

if not 'tifo' in d:
    d['tifo'] = "Forza Catania"

print(d['tifo'])



print(len(d))
print(sorted(d))

for key in d.keys():
    print(key, d[key])

gender = d.pop('gender')

d.popitem()
d.clear()