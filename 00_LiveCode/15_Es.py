# *args e **kwargs

def prodotto(*numeri): #Omettendo l'asterisco la funzione accetterà un parametro singolo e qualora ne aggiungessimo altri andrà in errore, con l'asterisco andiamo a creare un iterabile dove potremmo inserire più parametri
    print(len(numeri))

prodotto("ciao", "paloma", "paurina")

##############################################################

def prodotto1(*numeri1):
    a = 1
    for el in numeri1:
        a *= el
    return a

print(prodotto1(5))
print(prodotto1(4, 5))
print(prodotto1(3, 2, 7))

##############################################################

def team(**amesquatra):
    print("Vi presento a me squatra")
    print("Ruoli previsti: ", amesquatra.keys())
    print("Ve la presento meglio: ")
    for role, name in amesquatra.items():
        print(role, name)

#team(Founder = "Mirko")
#team(Founder = "Mirko", Cofounder = "Francesco")
team(Founder = "Mirko", Cofounder = "Francesco", Ambassador = "Blanco")