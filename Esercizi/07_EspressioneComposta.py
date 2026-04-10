user = input("Inserisci l'username: ")
pwd = input("Inserisci la password: ")

if(user == "admin" and pwd != ""):
    print("Login OK")
else:
    print("Login Failed")