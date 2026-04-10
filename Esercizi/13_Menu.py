string = input("Inserisci un comando: ")

match string:
    case "Start":
        print("Hai scelto start")
    case "Stop":
        print("Hai scelto stop")
    case "Exit":
        print("Hai scelto exit")
    case _:
        print("Unknown command")