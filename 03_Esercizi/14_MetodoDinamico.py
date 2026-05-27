class Playlist:
    def __init__(self, name, desc, songs = []):
        self.name = name
        self.desc = desc
        self.songs = songs

    def play(self):
        print(f"Stai ascoltando la playlist: {self.name}")

pl1 = Playlist("Estate 2025", "Le canzoni dell'estate", ['Labirinto', 'Niente canzoni d\'amore'])

scelta = input("Quale metodo vuoi eseguire? (scrivi 'play'): ")

azione = getattr(pl1, scelta, None) # getattr() restituisce l'attributo di un oggetto in base al nome passato come stringa. Se l'attributo non esiste, restituisce None (o un valore di default se specificato).

if azione:
    azione()
else:
    print("Metodo non trovato o non eseguibile.")