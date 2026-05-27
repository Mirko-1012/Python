def filtroProcedurale(lista):
    risultato = []
    for n in lista: 
        if n > 10:
            risultato.append(n) # Aggiunge il numero alla lista dei risultati se è maggiore di 10
    return risultato

numeri = [5, 12, 7, 20, 6]

print(f"Modo Procedurale: {filtroProcedurale(numeri)}") # Stampa i numeri maggiori di 10 usando la funzione procedurale

########################################################################

class numberFilter:
    def __init__(self, lista_iniziale):
        self.numeri = lista_iniziale
    
    def analizza(self, limite):
        risultati_finali = []

        for n in self.numeri:
            if n > limite:
                risultati_finali.append(n) # Aggiunge il numero alla lista dei risultati se è maggiore del limite specificato
        return risultati_finali
    

dati = [5, 12, 7, 20, 6]
filtro = numberFilter(dati)

risultato = filtro.analizza(10) # Chiama il metodo analizza per filtrare i numeri maggiori di 10 usando la classe OOP
print(f"Modo OOP: {risultato}")

########################################################################

numeri_1 = [5, 12, 7, 20, 6]

risultato_funzionale = list(filter(lambda x: x > 10, numeri_1)) # Usa la funzione filter con una lambda per filtrare i numeri maggiori di 10 in modo funzionale

print(f"Modo Funzionale: {risultato_funzionale}")