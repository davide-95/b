from Libro import Libro
from Scaffale import Scaffale

class Piano:
    def __init__(self):
        self.lista_scaffali = []
        for val in range(1,31):
            scaffale = Scaffale("SC" + str(val))
            self.lista_scaffali.append(scaffale)

    def addLibro(self, codicescaffale, ripiano, libro):
            for scaffale in self.lista_scaffali:
                if scaffale.codice == codicescaffale:
                    libro.setPiano(self)
                    scaffale.addLibro(ripiano, libro)
                # aggiungiamo il libro al ripiano dello scaffale

    def contiene(self, codicescaffale, ripiano, libro):
        for scaffale in self.lista_scaffali:
            if scaffale.codice == codicescaffale:
                return scaffale.contiene(ripiano, libro)
        return False
    #se non ha trovato nessun scafale corretto ritorna false

    def getLibri(self, codicescaffale):
        for scaffale in self.lista_scaffali:
            if scaffale.codice == codicescaffale:
                return  scaffale.getLibri()

    #per ogni scaffale con il codice scaffale uguale codice scaffale, ritorna tutti i libri

    def getLibro(self, autore, titolo):
        for scaffale in self.lista_scaffali:
            if scaffale.getLibro(autore, titolo):
                return  scaffale.getLibro(autore, titolo)
