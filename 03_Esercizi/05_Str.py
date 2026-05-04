class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} - Grade: {self.grade}"

s1 = Student("Alice", 28)

print(s1)