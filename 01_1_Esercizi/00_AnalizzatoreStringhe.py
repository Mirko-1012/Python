testo = input("Inserisci la stringa da analizzare: ")

parole = len(testo.split()) # Conta il numero di parole dividendo la stringa in base agli spazi e contando gli elementi risultanti
vocali_str = "aeiouAEIOU"
cont_vocali = 0
cont_consonanti = 0
cont_maiuscole = 0
cont_spazi = 0
cont_speciali = 0

for char in testo:
    if char.isupper(): # Verifica se il carattere è una lettera maiuscola
        cont_maiuscole += 1
    
    if char.isspace(): # Verifica se il carattere è uno spazio (spazio, tab, ecc.)
        cont_spazi += 1
    
    if char.isalpha(): # Verifica se il carattere è una lettera (vocale o consonante)
        if char in vocali_str:
            cont_vocali += 1
        else:
            cont_consonanti += 1
    elif not char.isdigit() and not char.isspace(): # Se il carattere non è una lettera, né un numero, né uno spazio, lo consideriamo speciale
        cont_speciali += 1

print(f"\n--- Risultati Analisi ---")
print(f"Parole: {parole}")
print(f"Vocali: {cont_vocali}")
print(f"Consonanti: {cont_consonanti}")
print(f"Maiuscole: {cont_maiuscole}")
print(f"Spazi: {cont_spazi}")
print(f"Caratteri speciali: {cont_speciali}")