#3. Crie uma classe chamada Carro com um método dirigir(). Em seguida, crie duas subclasses,
#CarroGasolina e CarroEletrico, cada uma com sua própria implementação de dirigir().
#Demonstre o polimorfismo passando instâncias de ambas as subclasses para uma função que recebe
#um objeto Carro.

# ============================================= #

class Carro:
    def dirigir(self):
        return ""

class CarroGasolina(Carro):
    def dirigir(self):
        return "Dirigindo carro a gasolina"

class CarroEletrico(Carro):
    def dirigir(self):
        return "Dirigindo carro elétrico"

def testar(carro):
    print(carro.dirigir())

testar(CarroGasolina())
testar(CarroEletrico())