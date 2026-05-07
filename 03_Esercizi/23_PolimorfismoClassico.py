class Car:
    def steer(self):
        print("La macchina sta sterzando con il volante")

class Moto:
    def steer(self):
        print("La moto sta sterzando con il manubrio")

lista = []

c1 = Car()
lista.append(c1)

m1 = Moto()
lista.append#(m1)

print(lista)

for el in lista:
    el.steer()
