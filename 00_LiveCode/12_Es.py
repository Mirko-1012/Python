command = input("Inserisci un comando: ")

match command:
    case "Start":
        print("Il programma sta iniziando")
    case "Stop":
        print("Il programma si è fermato")
    case "Help":
        print("Forza Catania")
    case _:
        print("Forza Palermo")