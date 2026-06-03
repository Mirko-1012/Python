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
    maschera = "*" * lunghezza 
    tentativi_gioco = [] 

    print(f"\nLa parola da indovinare è: {maschera} ({lunghezza} lettere)")

    for t in range(3):
        proposta = input(f"\nTentativo {t+1}/3 - Indovina la parola: ").strip().upper()
        tentativi_gioco.append(proposta)

        if proposta == parola_segreta:
            print(" Hai indovinato la parola!")
            maschera = parola_segreta
            break
        else:
            print("Sbagliato!")
            
            nuova_maschera = ""
            for el in range(lunghezza):
                if el < len(proposta) and proposta[el] == parola_segreta[el]:
                    nuova_maschera += parola_segreta[el]
                else:
                    nuova_maschera += maschera[el]
            
            maschera = nuova_maschera
            
            print(f"Stato attuale: {maschera}") 
            print(f"Parole provate finora: {tentativi_gioco}")

    if maschera == parola_segreta: 
        print(f"\nVITTORIA! La parola era: {parola_segreta}")
    else:
        print(f"\nGAME OVER. La parola era: {parola_segreta}")