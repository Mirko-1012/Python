# Funzione ricorsiva

def factorial(n):
    # Caso base 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)