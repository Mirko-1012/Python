username = input("Inserisci il nome utente: ")
password = input("Inserisci la password: ")

if username != "" and len(password) >= 6:
    print("Valid")
else:
    print("Invalid")