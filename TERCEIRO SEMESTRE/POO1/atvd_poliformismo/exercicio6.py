#6. Crie uma classe chamada ContaBancaria com os métodos deposito() e retirada(). Crie
#duas subclasses: ContaPoupanca e ContaCorrente. Cada uma dessas subclasses deve ter sua
#própria taxa de juros (a taxa de juros da Conta Poupança é maior que a da Conta Corrente).

# ========================================= #

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        self.saldo -= valor

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo=0):
        super().__init__(saldo)
        self.juros = 0.05

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo=0):
        super().__init__(saldo)
        self.juros = 0.02