pwd = "python"
pwd_inserita = input("Inserisci la password: ")

while (pwd != pwd_inserita):    
    print("Error")
    pwd_inserita = input("Inserisci la password: ")
else:
    print("Access granted")