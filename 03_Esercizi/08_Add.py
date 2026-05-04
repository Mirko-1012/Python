class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def __add__(self, other_course):
        nuovo_corso = Course(f"{self.title} e {other_course.title}")
        nuovo_corso.students = self.students + other_course.students
        return nuovo_corso

    def __str__(self):
        return f"Corso: {self.title} | Studenti: {self.students}"


c1 = Course("Python Base")
c1.students = ["Mirko", "Blanco"]

c2 = Course("Python Avanzato")
c2.students = ["Matteo", "Gioele"]

corso_completo = c1 + c2

print(corso_completo)