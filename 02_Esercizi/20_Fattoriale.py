def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # La funzione chiama se stessa con un valore di n decrementato fino a raggiungere 0, momento in cui restituisce 1. Il risultato finale è il prodotto di tutti i numeri da n a 1.

print(factorial(5))