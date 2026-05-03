parola_segreta = ""
tentativi_validazione = 0
valida = False

while tentativi_validazione < 3:
    input_iniziale = input("Inserisci la parola da far indovinare: ").strip().upper()
    if input_iniziale.isalpha() and len(input_iniziale) > 0:
        parola_segreta = input_iniziale
        valida = True
        break
    else:
        tentativi_validazione += 1
        print(f"Parola non valida! (Tentativi rimasti: {3 - tentativi_validazione})")

if not valida:
    print("Inizializzazione fallita.")
else:
    lunghezza = len(parola_segreta)
    maschera = ["*"] * lunghezza
    tentativi_gioco = []

    print(f"\nLa parola da indovinare è: {''.join(maschera)} ({lunghezza} lettere)")

    for t in range(3):
        proposta = input(f"\nTentativo {t+1}/3 - Indovina la parola: ").strip().upper()
        tentativi_gioco.append(proposta)

        if proposta == parola_segreta:
            print("🎉 GRANDE! Hai indovinato la parola!")
            maschera = list(parola_segreta)
            break
        else:
            print("Sbagliato!")
            for i in range(min(len(proposta), lunghezza)):
                if proposta[i] == parola_segreta[i]:
                    maschera[i] = parola_segreta[i]
            
            print(f"Stato attuale: {''.join(maschera)}")
            print(f"Parole provate finora: {tentativi_gioco}")

    if "".join(maschera) == parola_segreta:
        print(f"\nVITTORIA! La parola era: {parola_segreta}")
    else:
        print(f"\nGAME OVER. La parola era: {parola_segreta}")