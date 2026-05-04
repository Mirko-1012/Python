class Playlist:
    description = "Class used to represent playlist"
    
    def __init__(self, name, pl_descr, songs=[]):
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs


pl1 = Playlist ("Estate 2025", "Le canzoni di quando ho conosciuto Morena", ['Maracaibo', 'Danza Kuduro'])
pl2 = Playlist ("Estate 2023", "Le canzoni di quando ho conosciuto Morena", "Cinciuncian")

print(type(pl1))
print(isinstance(pl1, Playlist))
print(isinstance(pl1, int))

print("Has title?", hasattr(pl1, "name"))
print("Has promotion?", hasattr(pl1, "promotion"))

print(list(Playlist.__dict__))
print(list(pl1.__dict__))

a = input("Inserisci l'attributo cercato nella playlist: ")
print(f"Risultato: {hasattr(pl1, a)}")

#################################################################################################################

print(pl1.name) # Hardcoded
print(getattr(pl1, "name")) #Softcoded

a = input("Inserisci attributo: ")
if hasattr(pl1, a):
    print(getattr(pl1, a, "attributo non trovato"))
else:
    b = input("Attributo on trovato inserire il valore che si vuole associare: ")
    setattr(pl1, a, b)
    
print(getattr(pl1, a))