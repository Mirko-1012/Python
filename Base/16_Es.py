def saluto(nome):
    global b
    print(f"Ciao, {nome}")
    b = 343 # Variabile locale (ambito di visibilità) (funziona solamente dentro la funzione dato che è una variabile locale) # Scope
    print(b) # Così funziona perché all'interno della funzione

b = 5
saluto("Mirko")
print(b)