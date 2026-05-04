class Playlist:
    description = "Class used to represent playlist"
    
    def __init__(self, name, pl_descr, songs=[]):
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs

    def __add__(self, other):
        if isinstance(other, Playlist):
            nuovoNome = self.name + "+" + other.name
            nuovaPldescr = f"Playlist creata automaticamente unendo {self.name} e {self.name}"
            nuoveSongs = self.songs + other.songs
            return Playlist(nuovoNome, nuovaPldescr, nuoveSongs)
        else:
            print("Non posso sommare gli elementi richiesti")
            return
    
    def __str__(self):
        a= f'''Titolo della Playlist: {self.name}\n
            {self.pl_descr}
            questa playlist contiene esattamente {len(self.songs)} canzoni \n
            {self.songs}
            '''
        return a
        

pl1 = Playlist ("Estate 2025", "Le canzoni di quando ho conosciuto Morena", ['Maracaibo', 'Danza Kuduro'])
pl2 = Playlist ("Estate 2023", "Le canzoni di quando ho conosciuto Alessia", ['Volare', 'Macarena', 'Buoni o Cattivi'])

pl3 = pl1 + pl2

print(pl3.name)
print(pl3.pl_descr)
print(pl3.songs)
print(pl1)