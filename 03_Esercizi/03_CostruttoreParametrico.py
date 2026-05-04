class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print(f"Oggetto creato: Studente {self.name} con voto {self.grade}")


s1 = Student("Mirko", 10)
s2 = Student("Blanco", 8)

print(f"Il primo studente si chiama: {s1.name}")