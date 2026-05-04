class Vehicle:
    type = "Car"

    def __init__(self, model):
        self.model = model

v1 = Vehicle("Panda")
v2 = Vehicle("308")

print(f"V1 (Modello: {v1.model}) - Tipo: {v1.type}")
print(f"V2 (Modello: {v2.model}) - Tipo: {v2.type}")

v1.type = "Electric Vehicle"

print(f"Classe (Vehicle.type): {Vehicle.type}")

print(f"V1 (Modello: {v1.model}) - Tipo: {v1.type}")
print(f"V2 (Modello: {v2.model}) - Tipo: {v2.type}")

print(v1.__dict__, v2.__dict__)