class Student:
    description = "This class is supposed to be used anytime you will create a new student" # Class Attributes
    
    def __init__(self, name, surname, age = 999, course = 99): # Costruttore
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course

        self.fullname = self.name + " " + self.surname
        # Instance Attributes

    def __eq__(self, other): # Metodi speciali o magici
        if isinstance(other, Student):
            if(self.name == other.name and self.surname == other.surname and self.age == other.age):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Student):
            return True # Da rivedere
        else: 
            print("Somma non fattibile")
            return None




s1 = Student("Salvatore", "Pappalardo", 15, "WebDeveloper")
s2 = Student("Salvatore", "Pappalardo", 45, "WebDeveloper")
s3 = Student("Salvatore", "Pappalardo", 15, "CyberSecurity")

print(s1 == s2) # False. L'età è diversa
print(s1 == s3) # True. Anche se il corso è diverso stampa true
print(s1 == 5) #False. Non sono della stessa classe