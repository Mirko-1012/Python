numbers = [1, 2, 3, 4]

doubled = list(map(lambda x : x * 2, numbers)) 

print(doubled)

# La funzione lambda prende un argomento x e restituisce il suo doppio. 
# La funzione map applica questa funzione a ogni elemento della lista numbers, 
# restituendo un iteratore che viene convertito in una lista con la funzione list().