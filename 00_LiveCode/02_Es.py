frutti = ["ananas", "mela"]
frutti.append("fragola") # Aggiunge un elemento alla fine della lista

print(frutti)
print(len(frutti))

a = frutti.pop() # Rimuove l'ultimo elemento della lista e lo restituisce, se vuoi rimuovere un elemento specifico puoi passare l'indice come argomento a pop
frutti.pop() # 
print(a)
print(frutti)

frutti.clear() # Rimuove tutti gli elementi dalla lista, lasciando una lista vuota

print(frutti)