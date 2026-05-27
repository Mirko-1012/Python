class Car:
    def steer(self):
        print("La macchina sta sterzando con il volante")

class Moto:
    def steer(self):
        print("La moto sta sterzando con il manubrio")

lista = []

c1 = Car()
lista.append(c1) # aggiungo un oggetto di tipo Car alla lista

m1 = Moto()
lista.append#(m1) # aggiungo un oggetto di tipo Moto alla lista

print(lista)

for el in lista: # scorro la lista e chiamo il metodo steer() per ogni elementos
    el.steer()
