class CarSteering:
    def turn(self):
        return "Giro il volante"

class BikeSteering:
    def turn(self):
        return "Inclino il manubrio"

class Vehicle:
    def __init__(self, model, steering_system):
        self.model = model
        self.steering_system = steering_system

    def engage_steering(self):
        print(f"--{self.model}--")
        print(f"{self.steering_system.turn()}")

    
volante = CarSteering()
manubrio = BikeSteering()

auto = Vehicle("Berlina", volante)
moto = Vehicle("Sportiva", manubrio)

auto.engage_steering()
moto.engage_steering()