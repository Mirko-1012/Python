class Student:
    school = "Steve Jobs Academy"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Mirko", 10)

print(dir(s1))

print(s1.__dict__)

print(Student.__dict__)