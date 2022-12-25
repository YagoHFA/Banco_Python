from cliente import Cliente

class Conta:
    
    def __init__(self):
        self.saldo = 0
        self._extrato = "" 
       


    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            self._extrato += "Depositado R$%.2f" % valor + "\n"
            self.dayLimit = 0
        else:
            raise IndexError ("Por favor deposite um valor valido")    
            
    def sacar(self, valor):
        if self.dayLimit < 3:
            if valor <= 500 and valor > 0  and valor <= self.saldo:
                self.saldo -= valor
                self.dayLimit += 1
                self._extrato += "Sacado R$%.2f" % valor + "\n"
            else:
                raise IndexError ("Por favor retire um valor valido")             
        else:
            raise IndexError("Limite de saque atingido")

    def extrato(self):
        return str(self._extrato + "\n" + "Saldo atual: R$%.2f" % self.saldo    ) 