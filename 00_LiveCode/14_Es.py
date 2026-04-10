def saluto(nome: str):
    print(f"ciao, {nome}!")


print("qui inizia il mio programma")
saluto("Mirko")
saluto("Gino")
saluto("Pino")

######################################################################

def moltiplicazione(a, b, c = 5): # Parametri
    if a == 3:
        return 3
    else:
        return a * b * c
    


print(moltiplicazione(3, 2, 6)) # Argomenti # Positional argument
print(moltiplicazione(a = 7, c = 5, b = 4)) # Keyword argument
print(moltiplicazione(7, c = 2, b = 3)) # Mixed