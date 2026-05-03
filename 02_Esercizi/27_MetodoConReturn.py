class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_description(self):
        return f"Profilo Utente: {self.name}, Età: {self.age} anni."

utente = Person("Mirko", 19)

descrizione = utente.get_description()

print(f"Ho ricevuto questi dati: {descrizione}")