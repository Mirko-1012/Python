class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def describe(self):
        print(f"Veicolo: {self.model}, Anno: {self.year}")
        
class Car(Vehicle):
    def __init__(self, model, year, doors = 5):
        super().__init__(model, year)
        self.doors = doors

    def describe_car(self):
        self.describe()
        print(f"Porte: {self.doors}")


c1 = Car("Fiat", 2012, 7)
c2 = Car("BMW", 2023, 3)

c1.describe_car()
c2.describe_car()
