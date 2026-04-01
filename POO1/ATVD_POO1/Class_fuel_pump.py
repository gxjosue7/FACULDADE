class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        if litros > self.quantidadeCombustivel:
            print("Combustível insuficiente.")
        else:
            self.quantidadeCombustivel -= litros
            print(f"Abastecido {litros:.2f} litros.")

    def abastecerPorLitro(self, litros):
        if litros > self.quantidadeCombustivel:
            print("Combustível insuficiente.")
        else:
            valor = litros * self.valorLitro
            self.quantidadeCombustivel -= litros
            print(f"Abastecido {litros:.2f} litros. Valor: R$ {valor:.2f}")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_tipo):
        self.tipoCombustivel = novo_tipo

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade


bomba = BombaCombustivel("Gasolina", 6.0, 500)

while True:
    print("\n1 - Abastecer por valor")
    print("2 - Abastecer por litro")
    print("3 - Alterar valor")
    print("4 - Alterar tipo")
    print("5 - Alterar quantidade")
    print("6 - Sair")
    op = input("Escolha: ")

    if op == "1":
        v = float(input("Valor: "))
        bomba.abastecerPorValor(v)
    elif op == "2":
        l = float(input("Litros: "))
        bomba.abastecerPorLitro(l)
    elif op == "3":
        nv = float(input("Novo valor: "))
        bomba.alterarValor(nv)
    elif op == "4":
        nt = input("Novo tipo: ")
        bomba.alterarCombustivel(nt)
    elif op == "5":
        nq = float(input("Nova quantidade: "))
        bomba.alterarQuantidadeCombustivel(nq)
    elif op == "6":
        break