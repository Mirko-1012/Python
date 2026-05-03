class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Ciao! Mi chiamo {self.name} e ho {self.age} anni.")

    def travel(self, partenza, arrivo):
        print(f"{self.name} sta viaggiando da {partenza} a {arrivo}.")

viaggiatore = Person("Marco", 28)

viaggiatore.travel("Milano", "Roma")