#2. Crie uma classe Animal com um método falar(). Em seguida, crie duas classes filhas,
#Cachorro e Gato, que herdam da classe Animal. Cada uma destas classes filhas deve ter seu
#próprio método falar() que retorne um som diferente (e.g. latidos para o cachorro e miados para
#o gato). Em seguida, crie uma lista de animais que inclua um cachorro e um gato. Por fim, itere
#sobre a lista e chame o método falar() de cada animal.

# =====================================#

class Animal:
    def falar(self):
        return ""

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())
