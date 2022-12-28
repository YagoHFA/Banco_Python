from cliente import Cliente
from Extrato import Extrato

class Conta:
    
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._extrato = Extrato()
        self._numero = numero
        self._agencia = "0007"
        self._cliente = cliente
        
       

    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._extrato
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)   

    def sacar(self, valor):
        saldo = self.saldo
        exedeu_saldo = valor > saldo

        if exedeu_saldo:
            print("A operação falhou! você está com saldo insuficiente")
        elif valor >0:
            self._saldo-= valor
            print("Você realizou o saque com sucesso!")
            return  True
        else:
            print("A operação falhou o valor informado é invalido")
        return False

    def depositar(self, valor):
       
    
        if valor >0:
            self._saldo += valor
            print("Você realizou o deposito com sucesso!")
            return  True
        else:
            print("A operação falhou o valor informado é invalido")
            return False

