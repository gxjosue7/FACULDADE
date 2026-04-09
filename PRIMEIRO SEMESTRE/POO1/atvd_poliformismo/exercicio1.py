#1. Crie uma hierarquia de classes para animais, com uma classe mãe Animal e subclasses Cachorro,
#Gato e Peixe. Cada subclasse deve ter um método falar() que retorne uma string
#representando o som que o animal faz. Demonstre o polimorfismo chamando falar() nas
#instâncias de cada subclasse.

# ===================================================== #
class Animal:
    def falar(self):
        return ""

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

class Peixe(Animal):
    def falar(self):
        return "..."

a = Cachorro()
b = Gato()
c = Peixe()

print(a.falar())
print(b.falar())
print(c.falar())

