# Fare inserire età all'utente. 
# Se minorenne, stampare accesso vietato. 
# Se maggiorenne eseguire un ulteriore controllo. 
# Se età è minore di 35 stampare membro junior
# Se età è compresa tra 35 e 50 stampare membro mid. 
# Se età maggiore di 50 stampare membro senior.

eta = int(input("Inserisci l'età: "))

if(eta < 18):
    print("Accesso vietato")
else:
    if(eta < 35):
        print("Membro Junior")
    elif(eta <= 50):
        print("Membro Mid")
    else:
        print("Membro Senior")