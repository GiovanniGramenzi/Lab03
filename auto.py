class Auto:
    def __init__(self,codice,marca,modello,annoimm,numposti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.annoimm = annoimm
        self.numposti = numposti

    def __str__(self):
        return f'{self.codice},{self.marca},{self.modello},{self.annoimm},{self.numposti}'