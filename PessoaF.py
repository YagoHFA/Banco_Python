from datetime import datetime
from cliente import Cliente
class PessoaF(Cliente):


    def __init__(self, nome, dataNasc, cpf, endereco):
        self._cpf = cpf
        self.nome = nome
        self.dataNas = dataNasc
        super().__init__(endereco)