from Libro import Libro
from Ripiano import Ripiano



class Scaffale:
    def __init__(self, codicescaffale):
        self.lista_ripiani = []
        for val in range(1,11):
            nuovoripiano = Ripiano(10)
            self.lista_ripiani.append(nuovoripiano)
        self.codice = codicescaffale

    def addLibro(self, ripiano, libro):
            libro.setScaffale(self)
            self.lista_ripiani[ripiano - 1].addLibro(libro)

    def contiene(self, ripiano, libro):
        self.lista_ripiani[ripiano - 1].contiene(libro)

         #richiamo il contiene al richiamo meno 1

    def getLibri(self):
        libri = ''
        for idx, ripiano in enumerate(self.lista_ripiani):
            libri += 'Ripiano ' + str(idx + 1) + ' '
            for libro in ripiano.lista_libri:
                libri += libro.toString() + ' '
        return libri
            #questo da per ogni ripiano tutti i libri

    def getLibro(self, autore, titolo):
        for ripiano in self.lista_ripiani:
            if ripiano.getLibro(autore, titolo):
                return  ripiano.getLibro(autore, titolo)

