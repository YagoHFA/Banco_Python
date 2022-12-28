from PessoaF import PessoaF
from Transação import Transacao

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)

    def adc_conta(self, conta):
        self.contas.append(conta)    
         

    
        
        