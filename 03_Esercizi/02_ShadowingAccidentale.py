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

# __dict__ mostra gli attributi di istanza di v1 e v2. v1 ha un attributo 'type' che sovrascrive l'attributo di classe, mentre v2 non ha un attributo 'type' di istanza e quindi utilizza l'attributo di classe.