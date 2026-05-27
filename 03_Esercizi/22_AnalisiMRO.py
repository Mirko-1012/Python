class Flyer:
    def move(self):
        return "Sto volando!"

class Swimmer:
    def move(self):
        return "Sto nuotando!"

class DuckA(Flyer, Swimmer):
    pass

class DuckB(Swimmer, Flyer):
    pass

d1 = DuckA()
print(f"DuckA (Flyer, Swimmer): {d1.move()}") # Il metodo move() viene risolto in base all'ordine di eredità specificato nella definizione della classe DuckA, quindi viene chiamato il metodo move() della classe Flyer.
print(f"MRO DuckA: {DuckA.mro()}\n") # Il metodo mro() restituisce una lista che rappresenta l'ordine di risoluzione dei metodi (Method Resolution Order) per la classe DuckA. In questo caso, l'ordine sarà DuckA, Flyer, Swimmer, object.

d2 = DuckB()
print(f"DuckB (Swimmer, Flyer): {d2.move()}")
print(f"MRO DuckB: {DuckB.mro()}")