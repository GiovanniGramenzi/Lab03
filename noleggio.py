class Noleggio:
    def __init__(self,data,id_automobile,cognome_cliente,cod_n):
        self.data = data
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente
        self.cod_n = cod_n
    def __str__(self):
        return f'{self.data},{self.id_automobile}, {self.cognome_cliente} {self.cod_n}'