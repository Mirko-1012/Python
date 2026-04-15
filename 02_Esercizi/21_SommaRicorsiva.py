def sommaRicorsiva(n):
    if n == 0:
        return 0
    else:
        return n + sommaRicorsiva(n - 1)

print(sommaRicorsiva(int(input("Inserisci un numero: ")))) 