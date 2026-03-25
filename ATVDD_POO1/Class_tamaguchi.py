class Tamagushi:
    def __init__(self, nome, fome=50, saude=50, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = max(0, min(100, nova_fome))

    def alterar_saude(self, nova_saude):
        self.saude = max(0, min(100, nova_saude))

    def alterar_idade(self, nova_idade):
        self.idade = max(0, nova_idade)

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        valor = self.saude - self.fome
        if valor > 70:
            return "Muito Feliz"
        elif valor > 30:
            return "Ok"
        elif valor > 0:
            return "Triste"
        else:
            return "Crítico"

    def status(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Fome: {self.fome}")
        print(f"Saúde: {self.saude}")
        print(f"Humor: {self.calcular_humor()}")


nome = input("Digite o nome do seu Tamagushi: ")
pet = Tamagushi(nome)

while True:
    pet.status()
    print("\n1 - Alterar nome")
    print("2 - Alimentar (reduzir fome)")
    print("3 - Dar remédio (aumentar saúde)")
    print("4 - Envelhecer (aumentar idade)")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        novo_nome = input("Novo nome: ")
        pet.alterar_nome(novo_nome)

    elif escolha == "2":
        qtd = int(input("Quanto deseja reduzir a fome (0-100)? "))
        pet.alterar_fome(pet.fome - qtd)

    elif escolha == "3":
        qtd = int(input("Quanto deseja aumentar a saúde (0-100)? "))
        pet.alterar_saude(pet.saude + qtd)

    elif escolha == "4":
        anos = int(input("Quantos anos deseja envelhecer? "))
        pet.alterar_idade(pet.idade + anos)

    elif escolha == "5":
        break

    else:
        print("Opção inválida!")