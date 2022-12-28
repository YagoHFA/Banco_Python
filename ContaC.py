from ContaB import Conta

class ContaCorrente(Conta):

    def __init__(self,numero, cliente, limite = 500, limitS = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limitS

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.extrato.transacao if transacao['tipo'] == Saque.__name__])

        exedeu_limite = valor > self._limite
        exedeu_saques = numero_saques = self._limite_saques

        if exedeu_limite:
            print("O valor informado é maior que o limite")