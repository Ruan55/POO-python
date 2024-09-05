from enum import Enum
import os
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id: int, nome: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
        self.idade = idade

    def __str__(self) -> str:
        return (f"\n Id: {self.id}"
                f"\n Nome: {self.nome}"
                f"\n Salario: {self.salario}"
                f"\n Setor: {self.setor.value}"
                f"\n Sexo: {self.sexo.value}"
                f"\n Idade: {self.idade}")

funcionario1 = Funcionario(2313, "Fernanda", 3400, Setor.RECURSOS_HUMANOS, Sexo.FEMININO, 22)
funcionario2 = Funcionario(5435, "Ricardo", 2300, Setor.FINANCEIRO, Sexo.MASCULINO, 33)
funcionario3 = Funcionario(2346, "Paula", 4300, Setor.MARKETING, Sexo.FEMININO, 26)
funcionario4 = Funcionario(8762, "Osvaldo", 2500, Setor.VENDAS, Sexo.MASCULINO, 39)

print(funcionario1)
print(funcionario2)
print(funcionario3)
print(funcionario4)