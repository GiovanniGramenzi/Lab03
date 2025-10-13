from auto import Auto
from noleggio import Noleggio
from operator import attrgetter
class Autonoleggio:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.macchine=[]
        self.noleggi=[]

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
        auto_riordinate=sorted(self.macchine, key=attrgetter('marca'))
        return auto_riordinate






    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        for car in self.macchine:
            if car.codice == id_automobile:
                break
            else:
                raise Exception('auto non presente nel sistema')
        for noleggio in self.noleggi:
            if noleggio.id_automobile== id_automobile:
                raise Exception('auto già noleggiata')

        cod_n=f'N{len(self.noleggi)+1}'
        nuovo_nol=Noleggio(data,id_automobile,cognome_cliente,cod_n)
        self.noleggi.append(nuovo_nol)
        return nuovo_nol


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
