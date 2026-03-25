class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2


lado = float(input("Digite o lado do quadrado: "))
q = Quadrado(lado)

while True:
    print("\n1 - Ver lado")
    print("2 - Calcular área")
    print("3 - Alterar lado")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        print(f"Lado: {q.retornar_lado()}")

    elif op == "2":
        print(f"Área: {q.calcular_area():.2f}")

    elif op == "3":
        novo = float(input("Novo lado: "))
        q.mudar_lado(novo)

    elif op == "4":
        break

    else:
        print("Opção inválida!")