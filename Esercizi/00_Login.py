password_corretta = "123abc"
tentativo = 3

for counter in range(tentativo):
    password = input("Inserisci la password: ").strip().lower()

    if password == password_corretta:
        print("Login eseguito con successo")
        break
    else:
        print(f"Password errata. Hai ancora {tentativo - counter - 1} tentativi.\n")

else:
    print("Hai esaurito i tentativi.")