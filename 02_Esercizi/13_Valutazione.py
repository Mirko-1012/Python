def valutazione(voto):
    if voto >= 6:
        return "Pass"
    return "Fail"

voto_utente = float(input("Inserisci il voto: "))

esito = valutazione(voto_utente)
print(esito)