def filtraNumeri(lista):
    nuova_lista = []
    
    for numero in lista:
        if numero % 2 == 0:
            nuova_lista.append(numero) # Aggiungo solo i numeri pari alla nuova lista
    return nuova_lista # Restituisco la nuova lista filtrata

numeri = [10, 15, 20, 25, 30]

risultato = filtraNumeri(numeri)

print(f"Lista originale {numeri}")
print(f"Lista aggiornata {risultato}")