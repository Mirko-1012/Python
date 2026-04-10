counter = 0

while True:
    number = int(input("Inserisci un numero: "))

    if number == 0:
        break

    if number > 0:
        counter += 1

print("Numeri positivi inseriti:", counter)