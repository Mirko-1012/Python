counter = 0
flag = False

while not flag:
    string = input("Inserisci una stringa: ")
    
    if string == "stop":
        flag = True
    else:
        counter += 1

print("Hai inserito", counter, "stringhe")