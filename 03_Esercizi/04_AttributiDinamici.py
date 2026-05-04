class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print(f"Oggetto creato: Studente {self.name} con voto {self.grade}")


s1 = Student("Mirko", 10)
s2 = Student("Blanco", 8)

s1.age = 20
print(f"Età di {s1.name}: {s1.age}")

#print(f"Età di {s2.name}: {s2.age}") da errore perché non abbiamo assegnato a s2 un'età
