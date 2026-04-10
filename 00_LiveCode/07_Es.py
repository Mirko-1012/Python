#truthy e falsy values

# TRUTHY ##############################################################

a = 3

if a: 
    print("Ciao a tutti")


# FALSY 0 - NONE - NULL - STRING - EMPTY COLLECTION ###################

b = input("Cosa stai pensando? ")

if b:
    print(f"Hai inserito il seguente messaggio\n{b}")
else:
    print("Messaggio non valido")

#######################################################################

lista_spesa = ["Casa"]

if lista_spesa:
    print(f"Le cose da comprare sono: {lista_spesa}")
else:
    print("la lista della spesa è vuota, niente da  visualizzare")


#######################################################################

c = int(input("Inserire l'età: "))

if(c < 18):
    print("Utente Minorenne")
elif(c < 30):
    print("Utente Giovane")
elif(c < 60):
    print("Utente meno Giovane")
else:
    print("me nanno")

#######################################################################

d = int(input("Inserire l'età: "))

if(a < 18):
    is_adult = False
else:
    is_adult = True


is_ad = False if d < 18 else True

