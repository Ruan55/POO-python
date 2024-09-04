import os
os.system("cls || clear")

# Criando classe endereço
class Endereco:
    # Criando um construtor
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
    
    # Semelhante ao toString()
    def __str__(self) -> str:
        return (f' \n Logradouro: {self.logradouro}' 
               f'\n Numero: {self.numero}')

# Criando a classe Aluno.
class Aluno:
    # Criando um construtor.
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    # Semelhante ao toString()
    def __str__(self) -> str:
        return (f'Nome: {self.nome}' 
                f'\n Idade: {self.idade}'
                f'\n Endereço: {self.endereco}')

# Instanciar classe.
# endereco = Endereco("Rua A", "52")
# aluno = Aluno("Ruan", 22, endereco)

aluno = Aluno("Ruan", 22, Endereco("Rua A", "52"))

print(aluno)