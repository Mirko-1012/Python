class Flyer:
    def fly(self):
        print("Sto volando")

class Swimmer:
    def fly(self):
        print("Sto volando sull'acqua")

class Duck(Flyer,Swimmer):
    pass # Il pass è un'istruzione che indica che non c'è nulla da eseguire, ma è necessario per evitare errori di sintassi.


paperino = Duck() 

paperino.fly()

for el in Duck.mro(): # Il metodo mro() restituisce una lista che rappresenta l'ordine di risoluzione dei metodi (Method Resolution Order) per la classe Duck. In questo caso, l'ordine sarà Duck, Flyer, Swimmer, object.
    print(el)