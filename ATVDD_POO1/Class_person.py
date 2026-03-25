class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            if self.idade < 21:
                self.altura += 0.05
            self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} m")


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

p = Pessoa(nome, idade, peso, altura)

while True:
    p.mostrar_dados()
    print("\n1 - Envelhecer")
    print("2 - Engordar")
    print("3 - Emagrecer")
    print("4 - Crescer")
    print("5 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        anos = int(input("Quantos anos deseja envelhecer? "))
        p.envelhecer(anos)

    elif op == "2":
        peso_add = float(input("Quantos kg deseja engordar? "))
        p.engordar(peso_add)

    elif op == "3":
        peso_sub = float(input("Quantos kg deseja emagrecer? "))
        p.emagrecer(peso_sub)

    elif op == "4":
        altura_add = float(input("Quanto deseja crescer (m)? "))
        p.crescer(altura_add)

    elif op == "5":
        break

    else:
        print("Opção inválida!")