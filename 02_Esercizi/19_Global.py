def numero(numero):
    global a
    a = 1
    print(a)

a = 5 
numero(a)
print(a) # Stampa 1, perché la variabile a è stata modificata all'interno della funzione numero() utilizzando la parola chiave global.

