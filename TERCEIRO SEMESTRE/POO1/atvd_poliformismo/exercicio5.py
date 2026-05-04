#5. Crie uma classe Empregado com um método pagar_salario(). Em seguida, crie duas classes
#filhas, EmpregadoHora e EmpregadoMes, que herdam da classe Empregado. Cada uma das
#classes filhas deve ter seu próprio método pagar_salario() que calcula o salário com base no
#número de horas trabalhadas ou no salário mensal, respectivamente. Em seguida, crie uma lista de
#funcionários que inclua um funcionário horista e um funcionário mensalista. Por fim, itere sobre a
#lista e chame o método pagar_salario() de cada funcionário.

# ============================================ #

class Empregado:
    def pagar_salario(self):
        return 0

class EmpregadoHora(Empregado):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def pagar_salario(self):
        return self.horas * self.valor_hora

class EmpregadoMes(Empregado):
    def __init__(self, salario):
        self.salario = salario

    def pagar_salario(self):
        return self.salario

funcionarios = [
    EmpregadoHora(40, 20),
    EmpregadoMes(3000)
]

for f in funcionarios:
    print(f.pagar_salario())