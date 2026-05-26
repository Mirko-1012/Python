# Iterabili

a = [1, 2, 3]
b = [4, 5, 19]

c = a + b
print(c)

#########################################################

d = ["Fragola", "Banana", "Cocco"]
print(sorted(d)) # sorted restituisce una nuova lista ordinata, lasciando la lista originale invariata
print(d)
d.sort() # sort ordina la lista originale, modificandola
print(d)

#########################################################

a = [1,2,3,2,3,2,3,4,5,6,2,2]

# Rimozioni

d.remove("Cocco") # Rimuove la prima occorrenza di "Cocco" nella lista, se non è presente solleva un errore

a.remove(5)
a.remove(2) # Il remove rimuove solo il primo dei tanti

while 2 in a:
    a.remove(2) # Rimuove tutte le occorrenze di 2 nella lista, finché 2 è presente in a