class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_lados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornar_lados(self):
        return self.ladoA, self.ladoB

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return 2 * (self.ladoA + self.ladoB)


ladoA = float(input("Digite o comprimento (m): "))
ladoB = float(input("Digite a largura (m): "))

ret = Retangulo(ladoA, ladoB)

while True:
    print("\n1 - Ver medidas")
    print("2 - Calcular área")
    print("3 - Calcular perímetro")
    print("4 - Alterar medidas")
    print("5 - Calcular pisos e rodapés")
    print("6 - Sair")

    op = input("Escolha: ")

    if op == "1":
        a, b = ret.retornar_lados()
        print(f"Comprimento: {a} m | Largura: {b} m")

    elif op == "2":
        print(f"Área: {ret.calcular_area():.2f} m²")

    elif op == "3":
        print(f"Perímetro: {ret.calcular_perimetro():.2f} m")

    elif op == "4":
        a = float(input("Novo comprimento: "))
        b = float(input("Nova largura: "))
        ret.mudar_lados(a, b)

    elif op == "5":
        area = ret.calcular_area()
        perimetro = ret.calcular_perimetro()
        print(f"Pisos necessários: {area:.2f} unidades")
        print(f"Rodapés necessários: {perimetro:.2f} m")

    elif op == "6":
        break

    else:
        print("Opção inválida!")