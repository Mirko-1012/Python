numeri = [1, 3, 6, -7, 5, 5, 8, 10, 52, 36, 0, 78]

for numero in numeri:
    if(numero < 0):
        continue
    elif(numero == 0):
        break
    elif(numero > 10):
        print(numero)
    
    