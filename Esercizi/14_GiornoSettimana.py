day = input("Inserisci un giorno: ")

match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("Weekday")
    case "Saturday"|"Sunday":
        print("Weekend")
    case _:
        print("Unknown command")