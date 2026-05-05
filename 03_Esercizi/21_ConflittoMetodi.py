class Flyer:
    def fly(self):
        print("Sto volando")

class Swimmer:
    def fly(self):
        print("Sto volando sull'acqua")

class Duck(Flyer,Swimmer):
    pass


paperino = Duck()

paperino.fly()

for el in Duck.mro():
    print(el)