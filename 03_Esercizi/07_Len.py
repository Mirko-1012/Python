class Course:
    def __init__(self, title, student_list):
        self.title = title
        self.students = student_list

    def __len__(self):
        return len(self.students)

students = ["Marco", "Mirko", "Gioele", "Matteo", "Blanco"]

c1 = Course("Programmazione Python", students)

print(f"Il corso '{c1.title}' ha {len(c1)} iscritti.")