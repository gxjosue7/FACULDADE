class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, km):
        gasto = km / self.consumo
        if gasto > self.combustivel:
            print("Combustível insuficiente para percorrer a distância.")
            self.combustivel = 0
        else:
            self.combustivel -= gasto
            print(f"Andou {km} km.")

    def obterGasolina(self):
        print(f"Combustível no tanque: {self.combustivel:.2f} litros")

    def adicionarGasolina(self, litros):
        self.combustivel += litros
        print(f"Adicionado {litros} litros.")


meuFusca = Carro(15)

while True:
    print("\n1 - Abastecer")
    print("2 - Andar")
    print("3 - Ver combustível")
    print("4 - Sair")
    op = input("Escolha: ")

    if op == "1":
        l = float(input("Litros: "))
        meuFusca.adicionarGasolina(l)
    elif op == "2":
        km = float(input("Quilômetros: "))
        meuFusca.andar(km)
    elif op == "3":
        meuFusca.obterGasolina()
    elif op == "4":
        break