from Biblioteca import Biblioteca



class GestioneBiblio:

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def start(self):

        while True:
            x = input(">")
            x_splitter = x.split(' ')
            #spezza la stringa in basa agli spazzi e crea una lista separata dagli spazi
            cmd = x_splitter[0]
            if cmd == "add":
                autore = x_splitter[1]
                titolo = x_splitter[2]
                piano = int(x_splitter[3])
                scaffale = x_splitter[4]
                ripiano = int(x_splitter[5])

                self.biblioteca.addLibro(piano, scaffale, ripiano, titolo, autore)

            elif cmd == "list":
                piano = int(x_splitter[1])
                scaffale = x_splitter[2]
                print(self.biblioteca.getlibri(piano, scaffale))

            elif cmd =="libro":
                autore = x_splitter[1]
                titolo = x_splitter[2]
                libro = self.biblioteca.contiene(autore, titolo)
                print(self.biblioteca.getposition(libro))

            elif cmd == 'quit':
                return
            else:
                print("comando non valido")

