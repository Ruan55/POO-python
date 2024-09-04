from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f'\n Nome: {self.nome}'
                f'\n Salario: {self.salario}'
                f'\n Salario final: {self.salario_final()}')

class Motoboy(Funcionario):
    # Acréscimo de 10%
    BONIFICACAO = 1.1
    
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
class Engenheiro(Funcionario):
    # Acréscimo em 20%
    BONIFICACAO = 1.2

    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Crea: {self.crea}")

# Instanciando a classe
motoboy1 = Motoboy("José", 1000)
print(motoboy1)

engenheiro1 = Engenheiro("Rodri", 1000, "Cfds2313")
print(engenheiro1)