class Playlist:
    def __init__(self, name, desc, songs = []):
        self.name = name
        self.desc = desc
        self.songs = songs

pl1 = Playlist ("Estate 2025", "Le canzoni dell'estate", ['Labirinto', 'Niente canzoni damore'])

nuovo_attributo = input("Inserisci attributo: ")

valore_attributo = input(f"Inserisci il valore per {nuovo_attributo}: ")

setattr(pl1, nuovo_attributo, valore_attributo) # setattr permette di aggiungere un nuovo attributo a un oggetto, specificando il nome dell'attributo e il suo valore.
    
print(pl1.__dict__) # stampa il dizionario degli attributi dell'oggetto pl1, mostrando tutti gli attributi e i loro valori.