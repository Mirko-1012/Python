# 1. Definizione della gerarchia
class Vehicle:
    def __init__(self):
        self.tipo = "Mezzo di trasporto"

class Car(Vehicle):
    def __init__(self):
        super().__init__() # Chiamata al costruttore della classe base 
        self.ruote = 4

auto = Car()

print(f"L'oggetto è una Car? {isinstance(auto, Car)}") # Verifica se 'auto' è un'istanza di Car
print(f"L'oggetto è anche un Vehicle? {isinstance(auto, Vehicle)}")  # Verifica se 'auto' è anche un'istanza di Vehicle (stampa True perché Car eredita da Vehicle)