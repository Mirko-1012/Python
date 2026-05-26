def sommaVariabile(*args): # Args serve a raccogliere un numero variabile di argomenti posizionali in una tupla
    somma = 0
    for numero in args: 
        somma += numero
    return somma
print(sommaVariabile(1, 2, 3)) 