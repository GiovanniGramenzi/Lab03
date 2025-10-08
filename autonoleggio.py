from auto import Auto
class Autonoleggio:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.macchine=[]

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            file = open(file_path, "r")
            for r in file:
                r=r.rstrip()
                macchina=r.split(',')

                codice=macchina[0]
                marca=macchina[1]
                modello=macchina[2]
                annoimm=macchina[3]
                numposti=macchina[4]
                car=Auto(codice,marca,modello,annoimm,numposti)
                self.macchine.append(car)
            print(self.macchine)


        except FileNotFoundError:
            print("File non trovato")

    def aggiungi_automobile(self, marca, modello, annoimm, numposti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        n=len(self.macchine)
        codice=f'A{n+1}'
        car=Auto(codice,marca,modello,annoimm,numposti)
        self.macchine.append(car)
        return car

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
