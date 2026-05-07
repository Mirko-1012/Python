def filtraNumeri(lista):
    for numeri in lista:
        if numeri % 2 == 0:
            lista.remove(numeri)

numeri = [1, 2, 3, 4, 5, 6]
filtraNumeri(numeri)
print(numeri)