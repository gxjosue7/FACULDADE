class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if isinstance(alimento, Macaco):
            print(f"{self.nome} tentou comer {alimento.nome}! Não permitido.")
        else:
            self.bucho.append(alimento)
            print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        print(f"{self.nome} tem no bucho: {self.bucho}")

    def digerir(self):
        self.bucho.clear()
        print(f"{self.nome} está digerindo e agora o bucho está vazio.")


m1 = Macaco("George")
m2 = Macaco("Chico")

alimentos = ["Banana", "Maçã", "Pão"]
for alimento in alimentos:
    m1.comer(alimento)
    m1.verBucho()
    m2.comer(alimento)
    m2.verBucho()

m1.digerir()
m1.verBucho()