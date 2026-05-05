class Vehicle:
    def accelerate(self):
        print("Il veicolo sta accelerando")

class Car:
    def accelerate(self):
        print("Il veicolo sta accelerando")

class SuperCar(Vehicle, Car):
    color = "Red"


pandino = SuperCar()

pandino.accelerate()