#Crie uma classe Pessoa com os atributos nome e idade. Crie uma classe Aluno que herda de
#Pessoa e adicione o atributo nota. Crie um método para imprimir as informações da Pessoa e um
#método para imprimir as informações do Aluno.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Nota: {self.nota}")


pessoa = Pessoa("Carlos", 30)
print("=== Pessoa ===")
pessoa.imprimir_info()

aluno = Aluno("Josué", 20, 9.5)
aluno.imprimir_info()
print("\n=== Aluno ===")