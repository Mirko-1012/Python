class Libro:
    def __init__(self, titolo, autore, casa_editrice, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.casa_editrice = casa_editrice
        self.__prezzo = prezzo

    def get_prezzo(self):
        return self.__prezzo
    
    def set_prezzo(self, nuovo_prezzo):
        if nuovo_prezzo >= 0:
            self.__prezzo = nuovo_prezzo
        else:
            print("Errore: il prezzo non può essere negativo")
    
    def __str__(self):
        return f"'{self.titolo}'di {self.autore} costa {self.__prezzo} €"
    

class Catalogo:
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione
        self.lista_libri = []
        self.__valore_totale = 0.0

    def get_valore_totale(self):
        return self.__valore_totale

    def set_valore_totale(self, valore):
        self.__valore_totale = valore

    def ricalcola_valore(self):
        totale = sum(libro.get_prezzo() for libro in self.lista_libri)
        self.set_valore_totale(totale)

    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)
        self.ricalcola_valore()
        print(f"Libro {libro.titolo} aggiunto con successo. Il nuovo totale è: {self.get_valore_totale()}")

    def rimuovi_libro(self, titolo_libro):
        for libro in self.lista_libri:
            if libro.titolo == titolo_libro:
                self.lista_libri.remove(libro)
                self.ricalcola_valore()
                print(f"Rimosso {titolo_libro}. Il nuovo totale è: {self.get_valore_totale()}")
                return
        print(f"Libro: {titolo_libro} non trovato")

    def __eq__(self, altro_catalogo):
        if not isinstance(altro_catalogo, Catalogo):
            return False
        
        return (self.lista_libri == altro_catalogo.lista_libri and self.__valore_totale == altro_catalogo.get_valore_totale())
    
    def __add__(self, altro_catalogo):
        nuovo_nome = f"Unione di {self.nome} e {altro_catalogo.nome}"
        nuovo_cat = Catalogo(nuovo_nome, "Catalogo unito")

        nuovo_cat.lista_libri = self.lista_libri + altro_catalogo.lista_libri
        nuovo_cat.__ricalcola_valore()
        return nuovo_cat
        
    
l1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "Bompiani", 25.0)
l2 = Libro("1984", "George Orwell", "Mondadori", 12.0)

mio_catalogo = Catalogo("Biblioteca Personale", "Libri del cuore")

mio_catalogo.aggiungi_libro(l1)
mio_catalogo.aggiungi_libro(l2)

mio_catalogo.rimuovi_libro("1984")