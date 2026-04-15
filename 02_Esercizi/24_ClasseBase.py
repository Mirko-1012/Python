class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Ciao! Mi chiamo {self.name} e ho {self.age} anni.")

persona1 = Person("Mirko", 19)
persona1.greet()