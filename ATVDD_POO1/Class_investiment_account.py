class ContaInvestimento:
    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxaJuros / 100

    def mostrarSaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta = ContaInvestimento(1000, 10)

for _ in range(5):
    conta.adicioneJuros()
    conta.mostrarSaldo()