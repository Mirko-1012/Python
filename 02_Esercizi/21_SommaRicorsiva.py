def sommaRicorsiva(n):
    if n == 0:
        return 0
    else:
        return n + sommaRicorsiva(n - 1) # La funzione chiama se stessa con un valore di n decrementato fino a raggiungere 0, momento in cui restituisce 0. Il risultato finale è la somma di tutti i numeri da n a 1.

print(sommaRicorsiva(int(input("Inserisci un numero: ")))) 