class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

    def status(self):
        print(f"\nCor: {self.cor}")
        print(f"Circunferência: {self.circunferencia}")
        print(f"Material: {self.material}")


cor = input("Digite a cor da bola: ")
circ = float(input("Digite a circunferência: "))
material = input("Digite o material: ")

bola = Bola(cor, circ, material)

while True:
    print("\n1 - Ver dados da bola")
    print("2 - Trocar cor")
    print("3 - Sair")

    op = input("Escolha: ")

    if op == "1":
        bola.status()

    elif op == "2":
        nova = input("Nova cor: ")
        bola.trocaCor(nova)
        print("Cor alterada!")

    elif op == "3":
        break

    else:
        print("Opção inválida!")