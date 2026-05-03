class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_promoted(self):
        return self.grade >= 60

registro = [
    Student("Blanco", 85),
    Student("Marco", 42),
    Student("Mirko", 70),
    Student("Gioele", 55)
]

print("Studenti promossi:")
for studente in registro:
    if studente.is_promoted():
        print(f"- {studente.name} con voto {studente.grade}")