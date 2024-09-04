import os
os.system("cls || clear")

class Pet:
    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def __str__(self) -> str:
        return (f'\n Nome: {self.nome}' 
                f'\n Idade: {self.idade}' 
                f'\n Raça: {self.raca}'
                f'\n Porte: {self.porte} '
                f'\n Alimentação: {self.alimentacao}')
    
pet1 = Pet("Doug", 2, "Husky", "Médio", "Ração Premier Fórmula para Cães Adultos de Raças Grandes Sabor Frango Light - 15kg.")
pet2 = Pet("Michael", 4, "Vira-lata", "Médio", "Ração N&D Raças Médias Adultos.")

print(pet1)
print(pet2)