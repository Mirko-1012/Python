class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def accelerate(self):
        print(f"Il veicolo {self.model} sta accelerando.")

class Car(Vehicle):
    def __init__(self, model, year, doors=5):
        super().__init__(model, year)
        self.doors = doors

    def accelerate(self):
        print(f"La Car {self.model} ({self.doors} porte) sta accelerando con il motore a scoppio.")

class superCar(Car):
    def __init__(self, model, year, doors=2, color="Red"):
        super().__init__(model, year, doors)
        self.color = color

    def accelerate(self):
        print(f"La superCar {self.color} {self.model} sta volando sull'asfalto!")

    def ex_accelerate(self):
        super().accelerate()

s1 = superCar("Ferrari Purosangue", 2024, 4, "Rosso Corsa")

s1.accelerate()
s1.ex_accelerate()