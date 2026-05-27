class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self): # Metodo speciale per definire la rappresentazione in stringa dell'oggetto
        return f"Student: {self.name} - Grade: {self.grade}"

s1 = Student("Mirko", 19)

print(s1)