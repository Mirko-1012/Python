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

    def drive(self):
        print(f"--{self.model}--")
        print(f"{self.steering_system.turn()}")

veicolo = Vehicle("Audi R8", CarSteering())
veicolo.drive()

veicolo.steering_system = BikeSteering()

veicolo.drive()