from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f'\n Logradouro: {self.logradouro}'
                f'\n Número: {self.numero}'
                f'\n Complemento: {self.cep}'
                f'\n Cep: {self.cep}'
                f'\n Cidade: {self.cidade}')

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f'\n Nome: {self.nome}'
                f'\n Telefone: {self.telefone}'
                f'\n Email: {self.email}'
                f'\n Salario: {self.salario}'
                f'\n Endereço: {self.endereco}')
    
    
class Engenheiro(Funcionario):

    BONIFICACAO = 1.5

    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Crea: {self.crea}")
    
class Medico(Funcionario):

    BONIFICACAO = 2.0

    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Crm: {self.crm}")
    
engenheiro1 = Engenheiro("Caio", "4455-7661", "Caio323@gmail.com", 3000, Endereco("Rua C", "56", "N/A", "3213213", "São Paulo"), "SFFR324")
medico1 = Medico("Maria", "5433-1233", "Maria22@gmail.com", 4000, Endereco("Rua K", "21", "N/A", "324324", "Rio de Janeiro"), "FSAD323")

print(engenheiro1)
print(medico1)