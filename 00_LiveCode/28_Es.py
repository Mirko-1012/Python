class Car:
    def accelerate(self):
        print("La macchina accelera col pedale")

class Moto:
    def accelerate(self):
        print("La moto accelera con la manopola")

class Bici:
    def accelerate(self):
        print("La bici accelera spigendo")

lista = []

c1 = Car()
lista.append(c1)

m1 = Moto()
lista.append#(m1) funziona ma è commentato perché si sottolinea in rosso

b1 = Bici()
lista.append#(b1)

print(lista)

for el in lista:
    el.accelerate()
