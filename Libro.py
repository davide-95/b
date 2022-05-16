class Libro:
    def __init__(self, titolo, autore):
        self.__titolo = titolo
        self.__autore = autore


    def setPiano(self, piano):
        self.piano = piano

    def setScaffale(self, scaffale):
        self.scaffale = scaffale

    def setRipiano(self, ripiano):
        self.ripiano = ripiano

    def getTitolo(self):
        return self.__titolo

    def getAutore(self):
        return self.__autore

    def getPiano(self):
        return self.piano

    def getScaffale(self):
        return self.scaffale

    def getRipiano(self):
        return self.ripiano

    def toString(self):
        return self.__autore + ", " + self.__titolo
    


