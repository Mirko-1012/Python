class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age

p1 = Person("Marta", 23)

print(p1.name)
print(p1.getAge())
#object._classname_privateattribute
#print(p1._Person__age) # Name Mangling
print(list(p1.__dict__))
#print(p1.__age)