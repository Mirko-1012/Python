class Student:
    description = "This class is supposed to be used anytime you will create a new student" # Class Attributes
    
    def __init__(self, name, surname, age = 999, course = 99): # Costruttore
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course

        self.fullname = self.name + " " + self.surname
        # Instance Attributes


s1 = Student("Tommaso", "Pappalardo", 32, "Web Developer")
print(s1)
print(s1.name)
print(s1.surname)
print(s1.fullname)
print(s1.age)


s2 = Student("Riccardino", "Fuffolo")
s2 = Student(surname = "Fuffolo", name = "Riccardino")
print(s2)
print(s2.name)
print(s2.surname)
print(s2.fullname)
print(s2.age)