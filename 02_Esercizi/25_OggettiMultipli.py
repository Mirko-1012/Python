# Riprendiamo la classe definita prima
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Ciao! Mi chiamo {self.name} e ho {self.age} anni.")

persona_a = Person("Alice", 30)

persona_b = Person("Bruno", 15)

persona_a.greet()
persona_b.greet()