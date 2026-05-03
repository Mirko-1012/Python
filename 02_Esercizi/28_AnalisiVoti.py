def calcola_media(lista_voti):
    if not lista_voti:
        return 0
    return sum(lista_voti) / len(lista_voti)

votiTotali = [45, 78, 62, 30, 95, 55, 88]

votiSufficienti = [v for v in votiTotali if v >= 60]

media = calcola_media(votiSufficienti)

print(f"Voti sufficienti: {votiSufficienti}")
print(f"Media dei voti sufficienti: {media:.2f}")