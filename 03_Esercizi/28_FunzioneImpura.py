def filtraNumeri(lista):
    for numeri in lista:
        if numeri % 2 == 0: # Se il numero è pari
            lista.remove(numeri) # Rimuove il numero dalla lista

numeri = [1, 2, 3, 4, 5, 6]
filtraNumeri(numeri)
print(numeri)