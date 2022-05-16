from Libro import Libro

class Toomanylibri(Exception):
    pass

class Ripiano:


    def __init__(self, numero):
        self.lista_libri =[]
        self.numero = numero


    def addLibro(self, libro):
        if len(self.lista_libri) == 10:
            raise Toomanylibri
        libro.setRipiano(self)

        self.lista_libri.append(libro)

        #sta dando se stesso al libro

    def contiene(self, libro):
        return libro in self.lista_libri


    def elencoLibri(self):
        for libri in self.lista_libri:
            print(libri.titolo, libri.autore)

    def getLibro(self, autore, titolo):
        for libro in self.lista_libri:
            if libro.getAutore() == autore and libro.getTitolo() == titolo:
                return libro