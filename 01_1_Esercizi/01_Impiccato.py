parola_segreta = ""
tentativi_validazione = 0
valida = False # Flag per indicare se la parola è stata validata correttamente

while tentativi_validazione < 3:
    input_iniziale = input("Inserisci la parola da far indovinare: ").strip().upper() # Rimuove spazi e converte in maiuscolo per uniformità
    if input_iniziale.isalpha() and len(input_iniziale) > 0: # Verifica che la parola sia composta solo da lettere e non sia vuota
        parola_segreta = input_iniziale # Assegna la parola segreta se è valida e imposta il flag a True
        valida = True
        break
    else:
        tentativi_validazione += 1
        print(f"Parola non valida! (Tentativi rimasti: {3 - tentativi_validazione})")

if not valida:
    print("Inizializzazione fallita.")
else:
    lunghezza = len(parola_segreta) # Calcola la lunghezza della parola segreta
    maschera = "*" * lunghezza # Crea una maschera iniziale con asterischi della stessa lunghezza della parola segreta
    tentativi_gioco = [] # Lista per tenere traccia delle parole proposte durante il gioco

    print(f"\nLa parola da indovinare è: {maschera} ({lunghezza} lettere)")

    for t in range(3):
        proposta = input(f"\nTentativo {t+1}/3 - Indovina la parola: ").strip().upper()
        tentativi_gioco.append(proposta) # Aggiunge la proposta alla lista dei tentativi

        if proposta == parola_segreta:
            print("🎉 GRANDE! Hai indovinato la parola!")
            maschera = parola_segreta # Aggiorna la maschera per mostrare la parola completa
            break
        else:
            print("Sbagliato!")
            
            nuova_maschera = "" # Stringa temporanea per costruire la nuova maschera dopo il tentativo
            for el in range(lunghezza): # Itera su ogni posizione della parola segreta
                if el < len(proposta) and proposta[el] == parola_segreta[el]: # Verifica se la lettera proposta è corretta e nella posizione giusta
                    nuova_maschera += parola_segreta[el] # Se è corretta, mostra la lettera al posto dell'asterisco
                else:
                    nuova_maschera += maschera[el] # Altrimenti, mantiene l'asterisco o la lettera già rivelata in quella posizione
            
            maschera = nuova_maschera # Aggiorna la maschera con le nuove lettere rivelate
            
            print(f"Stato attuale: {maschera}") 
            print(f"Parole provate finora: {tentativi_gioco}")

    if maschera == parola_segreta: 
        print(f"\nVITTORIA! La parola era: {parola_segreta}")
    else:
        print(f"\nGAME OVER. La parola era: {parola_segreta}")