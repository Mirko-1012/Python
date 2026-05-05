class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        f"Student: {self.name} - Grade: {self.grade}"

    def __eq__(self, other):
        if self.name == other.name and self.grade == other.grade:
            return True
        else: 
            return False


s1 = Student("Mirko", 19)
s2 = Student("Mirko", 19)
s3 = Student("Blanco", 25)

print(f"s1 è uguale a s2? {s1 == s2}") # True   
print(f"s1 è uguale a s3? {s1 == s3}") # False