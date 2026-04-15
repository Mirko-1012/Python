def sommaVariabile(*args):
    somma = 0
    for numero in args:
        somma += numero
    return somma
print(sommaVariabile(1, 2, 3))