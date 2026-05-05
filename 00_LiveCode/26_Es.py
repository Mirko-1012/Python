class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def accelerate(self):
        print(f"{self.model} sta accelerando")

    def sterzo(self, angolo):
        print(f"{self.model} sta sterzando di {angolo} gradi")
        
        
class Car(Vehicle):  # Sintassi: class classname(super name) # Ereditarietà
    def __init__(self, model, year, doors = 5):
        super().__init__(model, year)
        super().accelerate()
        self.doors = doors

    def accelerate(self):
        print(f"{self.model} sta accelerando, ti ricordo che hai una car a {self.doors} porte")

    def ex_accelerate(self):
        super().accelerate()


class superCar(Car):
    color = "Red"


class Motorcycle(Vehicle):
    def __init__(self, model, year, shifter = "Manuale"):
        super().__init__(model, year)



c1 = Car("Fiat", 2012, 7)
c2 = Car("BMW", 2023, 3)

c1.accelerate()
c1.ex_accelerate()
c2.sterzo(90)