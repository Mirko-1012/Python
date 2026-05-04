class Student:
    name = ""
    role = "student"
    description = "This class is supposed to be used anytime you will create a new student" # Class Attributes
    

s1 = Student()
s1.name = "Tommaso"
# s1.age = 19 # A differenza di altri linguaggi tipo C o Java anche se andiamo a inserire un attributo non presente nella classe funzionerà e stamperà comunque

s2 = Student()
s2.name = "Lorenzo"

# print(s1.age)
print(s1.name, s2.name)
print(s1.role, s2.role)
print(s1, s2)