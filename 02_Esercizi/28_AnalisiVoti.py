def calcola_media(lista_voti):
    if not lista_voti: # Se la lista è vuota, evita la divisione per zero e restituisce 0
        return 0
    return sum(lista_voti) / len(lista_voti) # Calcola la media sommando tutti i voti e dividendo per il numero di voti

votiTotali = [45, 78, 62, 30, 95, 55, 88]

votiSufficienti = [v for v in votiTotali if v >= 60] # Crea una nuova lista che contiene solo i voti sufficienti (>= 60)

media = calcola_media(votiSufficienti)

print(f"Voti sufficienti: {votiSufficienti}")
print(f"Media dei voti sufficienti: {media:.2f}")