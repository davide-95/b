from Piano import Piano
from Libro import Libro
class Biblioteca:

    def __init__(self):
        piano1 = Piano()
        piano2 = Piano()
        piano3 = Piano()
        self.piani = [piano1, piano2, piano3]

    def addLibro(self, piano, scaffale, ripiano, titolo, autore):
        add_libro = Libro(autore,titolo)
        scaffale = str(scaffale)
        ripiano = int(ripiano)

        self.piani[piano -1].addLibro(scaffale, ripiano, add_libro)


    def getAutore(self, titolo):
        for libro in self.lista_libri:
            if str(libro.titolo)  == str(titolo):
                print (str(libro.autore))
                break

    def getlibri(self, piano, scaffale,):
            return self.piani[piano -1].getLibri(scaffale)

    def contiene(self, autore, titolo):
        for piano in self.piani:
            if piano.getLibro(autore, titolo):
                return piano.getLibro(autore, titolo)

    def getposition(self, libro):
        idxpiano = self.piani.index(libro.getPiano()) + 1
        idxscaffale = libro.getPiano().lista_scaffali.index(libro.getScaffale()) + 1
        idxripiano = libro.getScaffale().lista_ripiani.index(libro.getRipiano()) + 1


        return str(idxpiano) + ' ' + 'SC'+ str(idxscaffale) + ' ' + str(idxripiano)




