def calcola_media(lista_voti):
    if not lista_voti:
        return 0
    return sum(lista_voti) / len(lista_voti)

voti_totali = [45, 78, 62, 30, 95, 55, 88]

voti_sufficienti = [v for v in voti_totali if v >= 60]

media = calcola_media(voti_sufficienti)

print(f"Voti sufficienti: {voti_sufficienti}")
print(f"Media dei voti sufficienti: {media:.2f}")