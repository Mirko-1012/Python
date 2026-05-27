class Student:
    school = "Steve Jobs Academy"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Mirko", 10)

print(dir(s1)) # dir serve per vedere tutti gli attributi e i metodi di un oggetto e stamperà ['__class__', '__delattr__' ecc...]

print(s1.__dict__) # __dict__ è un attributo speciale che contiene un dizionario con tutti gli attributi dell'istanza e i loro valori, quindi stamperà {'name': 'Mirko', 'grade': 10}

print(Student.__dict__) # __dict__ è un attributo speciale che contiene un dizionario con tutti gli attributi della classe e i loro valori, quindi stamperà {'school': 'Steve Jobs Academy', '__init__': <function Student.__init__ at 0x...>, '__str__': <function Student.__str__ at 0x...>, '__eq__': <function Student.__eq__ at 0x...>}