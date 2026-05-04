class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} - Grade: {self.grade}"

    def __eq__(self, other):
        return self.name == other.name and self.grade == other.grade


s1 = Student("Alice", 28)
s2 = Student("Alice", 28)
s3 = Student("Bruno", 25)

print(f"s1 è uguale a s2? {s1 == s2}") # True   
print(f"s1 è uguale a s3? {s1 == s3}") # False