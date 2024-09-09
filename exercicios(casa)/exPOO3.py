import os
os.system("cls || clear")

class IdadeNaoPermetidaError(Exception):
    pass

class IdadeInvalidaError(Exception):
    pass

class Idade:
    def __init__(self, maioridade: int, menoridade: int) -> None:
        self.maioridade = maioridade
        self.menoridade = menoridade
        self._idade = 18

    @property
    def idade(self):
        return self._idade
    
    def verificandoIdade(self) -> str:
        idadeUsuario = int(input("Digite a sua idade: "))
        try:
            self.__verificar_idade(idadeUsuario)
        except IdadeNaoPermetidaError as erro:
            return f"Caro usuario: {erro}"
        try:
            self.__verificar_valor_negativo(idadeUsuario)
        except IdadeInvalidaError as erro:
            return f"Caro usuario: {erro}"
        
        return f"Maior de idade! Já pode se alistar"

    def __verificar_idade(self, idade):
        if idade > 0 and idade < self._idade:
            raise IdadeNaoPermetidaError("Você ainda é menor de idade! Não pode se alistar!")
        elif idade >= 65:
            raise IdadeNaoPermetidaError("Você ultrapassou a idade máxima para se alistar")
        
    def __verificar_valor_negativo(self, idade):
        if idade <= 0:
            raise IdadeInvalidaError("Idade inválida! Por favor digite a idade corretamente!")
        
class maiorIdade(Idade):
    pass

class menorIdade(Idade):
    pass

maior_idade = maiorIdade(18, 23)
menor_idade = menorIdade(12, 16)

print(maior_idade.verificandoIdade())
print(menor_idade.verificandoIdade())