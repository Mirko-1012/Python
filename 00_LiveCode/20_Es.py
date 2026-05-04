class Student:
    description = "This class is supposed to be used anytime you will create a new student" # Class Attributes
    name = ""

    def saluta(self): # Il self è sempre obbligatorio
        print(f"Ciao a tutti, mi chiamo {self.name}!")

    
s1 = Student()
s1.name = "Lorenzo"

s2 = Student()
s2.name = "Pancrazio"

s1.saluta()
s2.saluta()

print(s1.description)

s1.description = "Questo studente è particolarmente attivo e sveglio"

print(s1.description)
print(Student.description)