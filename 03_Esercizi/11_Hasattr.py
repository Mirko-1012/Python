class Playlist:
    def __init__(self, name, desc, songs = []):
        self.name = name
        self.desc = desc
        self.songs = songs
    
def controlla_attributo(oggetto, nome_attributo):
    if hasattr(oggetto, nome_attributo):
        print(f"has attribute {nome_attributo}")
    else:
        print(f"missing attribute {nome_attributo}")

pl1 = Playlist ("Estate 2025", "Le canzoni dell'estate", ['Labirinto', 'Niente canzoni damore'])
pl2 = Playlist ("Napoli", "Le canzoni Napoletane", ['Fratm'])

controlla_attributo(pl1, "name")
controlla_attributo(pl2, "promotion")