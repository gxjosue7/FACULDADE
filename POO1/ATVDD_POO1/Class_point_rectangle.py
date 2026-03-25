class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def imprimir_ponto(p):
    print(f"({p.x}, {p.y})")

class Retangulo:
    def __init__(self, largura, altura, vertice):
        self.largura = largura
        self.altura = altura
        self.vertice = vertice

    def centro(self):
        return Ponto(self.vertice.x + self.largura/2, self.vertice.y + self.altura/2)


v = Ponto(0, 0)
r = Retangulo(10, 6, v)

while True:
    print("\n1 - Ver centro do retângulo")
    print("2 - Alterar largura e altura")
    print("3 - Sair")
    op = input("Escolha: ")

    if op == "1":
        c = r.centro()
        imprimir_ponto(c)

    elif op == "2":
        l = float(input("Nova largura: "))
        a = float(input("Nova altura: "))
        r.largura = l
        r.altura = a

    elif op == "3":
        break