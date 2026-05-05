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
print(f"DuckA (Flyer, Swimmer): {d1.move()}")
print(f"MRO DuckA: {DuckA.mro()}\n")

d2 = DuckB()
print(f"DuckB (Swimmer, Flyer): {d2.move()}")
print(f"MRO DuckB: {DuckB.mro()}")