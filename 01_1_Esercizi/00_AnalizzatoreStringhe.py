testo = input("Inserisci la stringa da analizzare: ")

parole = len(testo.split())
vocali_str = "aeiouAEIOU"
cont_vocali = 0
cont_consonanti = 0
cont_maiuscole = 0
cont_spazi = 0
cont_speciali = 0

for char in testo:
    if char.isupper():
        cont_maiuscole += 1
    
    if char.isspace():
        cont_spazi += 1
    
    if char.isalpha():
        if char in vocali_str:
            cont_vocali += 1
        else:
            cont_consonanti += 1
    elif not char.isdigit() and not char.isspace():
        cont_speciali += 1

print(f"\n--- Risultati Analisi ---")
print(f"Parole: {parole}")
print(f"Vocali: {cont_vocali}")
print(f"Consonanti: {cont_consonanti}")
print(f"Maiuscole: {cont_maiuscole}")
print(f"Spazi: {cont_spazi}")
print(f"Caratteri speciali: {cont_speciali}")