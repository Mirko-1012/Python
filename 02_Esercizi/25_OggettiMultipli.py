class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Ciao! Mi chiamo {self.name} e ho {self.age} anni.")

persona1 = Person("Alice", 30)

persona2 = Person("Bruno", 15)

persona1.greet()
persona2.greet()