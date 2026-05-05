# 1. Definizione della gerarchia
class Vehicle:
    def __init__(self):
        self.tipo = "Mezzo di trasporto"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.ruote = 4

auto = Car()

print(f"L'oggetto è una Car? {isinstance(auto, Car)}")
print(f"L'oggetto è anche un Vehicle? {isinstance(auto, Vehicle)}")