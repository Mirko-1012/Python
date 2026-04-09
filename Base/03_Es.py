# Iterabili

a = [1, 2, 3]
b = [4, 5, 19]

c = a + b
print(c)

#########################################################

d = ["Fragola", "Banana", "Cocco"]
print(sorted(d))
print(d)
d.sort() # Ordina in ordine alfabetico
print(d)

#########################################################

a = [1,2,3,2,3,2,3,4,5,6,2,2]

# Rimozioni

d.remove("Cocco")

a.remove(5)
a.remove(2) # Il remove rimuove solo il primo dei tanti

while 2 in a:
    a.remove(2)