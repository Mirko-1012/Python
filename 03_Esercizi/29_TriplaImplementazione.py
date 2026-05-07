def filtroProcedurale(lista):
    risultato = []
    for n in lista: 
        if n > 10:
            risultato.append(n)
    return risultato

numeri = [5, 12, 7, 20, 6]

print(f"Modo Procedurale: {filtroProcedurale(numeri)}")

########################################################################

class numberFilter:
    def __init__(self, lista_iniziale):
        self.numeri = lista_iniziale
    
    def analizza(self, limite):
        risultati_finali = []

        for n in self.numeri:
            if n > limite:
                risultati_finali.append(n)
        return risultati_finali
    

dati = [5, 12, 7, 20, 6]
filtro = numberFilter(dati)

risultato = filtro.analizza(10)
print(f"Modo OOP: {risultato}")

########################################################################

numeri_1 = [5, 12, 7, 20, 6]

risultato_funzionale = list(filter(lambda x: x > 10, numeri_1))

print(f"Modo Funzionale: {risultato_funzionale}")