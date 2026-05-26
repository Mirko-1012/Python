a = input("Inserisci la prima stringa: ").strip().lower() # strip() rimuove gli spazi bianchi all'inizio e alla fine della stringa, lower() converte la stringa in minuscolo
b = input("Inserisci la seconda stringa: ").strip().lower()

if(a == b):
    print("Equal")
else:
    print("Different")