from enum import Enum
import os
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Aluno:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\n Nome: {self.nome}"
                f"\n Idade: {self.idade}"
                f"\n Sexo: {self.sexo.value}")
    
# Instanciando classes
aluno1 = Aluno("Ruan", 22, Sexo.MASCULINO)

print(aluno1)