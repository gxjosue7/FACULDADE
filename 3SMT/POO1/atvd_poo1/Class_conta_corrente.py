class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado!")

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado!")
            return True
        else:
            print("Saldo insuficiente ou valor inválido!")
            return False

    def mostrar_saldo(self):
        print(f"Conta: {self.numero_conta} | Correntista: {self.nome_correntista} | Saldo: R$ {self.saldo:.2f}")


numero = input("Digite o número da conta: ")
nome = input("Digite o nome do correntista: ")
conta = ContaCorrente(numero, nome)

while True:
    print("\n1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Alterar nome do correntista")
    print("5 - Sair")

    op = input("Escolha: ")

    if op == "1":
        conta.mostrar_saldo()

    elif op == "2":
        valor = float(input("Valor do depósito: "))
        conta.deposito(valor)

    elif op == "3":
        valor = float(input("Valor do saque: "))
        conta.saque(valor)

    elif op == "4":
        novo = input("Novo nome: ")
        conta.alterarNome(novo)
        print("Nome alterado com sucesso!")

    elif op == "5":
        break

    else:
        print("Opção inválida!")