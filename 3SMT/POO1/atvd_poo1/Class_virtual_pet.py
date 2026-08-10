import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(20, 80)
        self.tedio = random.randint(20, 80)

    def alimentar(self, quantidade):
        self.fome = max(0, self.fome - quantidade)

    def brincar(self, tempo):
        self.tedio = max(0, self.tedio - tempo)

    def humor(self):
        valor = 100 - (self.fome + self.tedio)
        if valor > 70:
            return "Muito Feliz"
        elif valor > 30:
            return "Ok"
        else:
            return "Triste"

    def __str__(self):
        return f"{self.nome} | Fome: {self.fome} | Tédio: {self.tedio}"

b1 = Bichinho("Pingo")
b2 = Bichinho("Bolinha")
fazenda = [b1, b2]

while True:
    for b in fazenda:
        print(b, "| Humor:", b.humor())
    print("\n1 - Alimentar todos")
    print("2 - Brincar com todos")
    print("3 - Porta secreta (valores exatos)")
    print("4 - Sair")
    op = input("Escolha: ")

    if op == "1":
        qtd = int(input("Quantidade de comida: "))
        for b in fazenda:
            b.alimentar(qtd)
    elif op == "2":
        tempo = int(input("Tempo de brincadeira: "))
        for b in fazenda:
            b.brincar(tempo)
    elif op == "3":
        for b in fazenda:
            print(str(b))
    elif op == "4":
        break