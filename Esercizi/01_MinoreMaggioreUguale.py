a = 5

b = int(input("Inserisci il secondo numero: "))

print(f"La variabile a è uguale a {a}")
print(f"La variabile b è uguale a {b}")

if(a > b):
    print(f"{a} è maggiore di {b}")
elif(a == b):
    print(f"{a} è uguale a {b}")
else:
    print(f"{a} è minore di {b}")