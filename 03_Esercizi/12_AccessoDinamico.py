class Playlist:
    def __init__(self, name, desc, songs = []):
        self.name = name
        self.desc = desc
        self.songs = songs

pl1 = Playlist ("Estate 2025", "Le canzoni dell'estate", ['Labirinto', 'Niente canzoni damore'])

a = input("Inserisci attributo: ")

risultato = getattr(pl1, a, "Attributo non trovato") # getattr() permette di accedere dinamicamente agli attributi di un oggetto. Prende tre argomenti: l'oggetto, il nome dell'attributo come stringa e un valore di default opzionale da restituire se l'attributo non viene trovato.

print(risultato)