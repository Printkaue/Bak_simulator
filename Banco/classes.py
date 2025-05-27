#Classe das contas

class conta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"{self.titular} recebeu um depósito de R$ {valor:.2f}. O saldo é de: R$ {self.saldo:.2f}"

    def sacar(self, valor):
        if valor > self.saldo:
            return "Não é possível fazer a transação pois o saldo é insuficiente."
        else:
            self.saldo -= valor
            return f"{self.titular} sacou R$ {valor:.2f} da conta. Saldo atual: R$ {self.saldo:.2f}"

    def transferir(self, valor, outra_conta):
        if valor > self.saldo:
            return "Não é possível fazer a transação pois o saldo não é suficiente."
        else:
            self.saldo -= valor
            outra_conta.saldo += valor
            return f"{self.titular} enviou R$ {valor:.2f} para {outra_conta.titular}. Saldo da sua conta: R$ {self.saldo:.2f}. Saldo da outra conta: R$ {outra_conta.saldo:.2f}"
          
