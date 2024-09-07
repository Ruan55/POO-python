from abc import ABC, abstractmethod
from enum import Enum
import os
os.system('cls || clear')

class UnidadeFederativa(Enum):
    BAHIA = "Bahia"
    SAO_PAULO = "São Paulo"
    RIO_DE_JANEIRO = "Rio de Janeiro"

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Juridico"

class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (f"\n Logradouro: {self.logradouro}"
                f"\n Número: {self.numero}"
                f"\n Complemento: {self.complemento}"
                f"\n Cep: {self.cep}"
                f"\n Cidade: {self.cidade}"
                f"\n Unidade Federativa: {self.uf.value}")
    
class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\n Id: {self.id}"
                f"\n Nome: {self.nome}"
                f"\n Telefone: {self.telefone}"
                f"\n Email: {self.email}"
                f"\n Endereco: {self.endereco}")
    
class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadocivil = estadocivil
        self.datanascimento = datanascimento

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Sexo: {self.sexo.value}"
                f"\n Estado Civil: {self.estadocivil.value}"
                f"\n Data de Nascimento: {self.datanascimento}")
    
class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Cpf: {self.cpf}"
                f"\n Rg: {self.rg}"
                f"\n Matricula: {self.matricula}"
                f"\n Setor: {self.setor.value}"
                f"\n Salario: {self.salario}")
    
class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoestadual = inscricaoestadual

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Cnpj: {self.cnpj}"
                f"\n Inscrição Estadual: {self.inscricaoestadual}")

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, protocoloatendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento)
        self.protocoloatendimento = protocoloatendimento

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Protocolo de Atendimento: {self.protocoloatendimento}")
    
class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str, contratoinicio: str, contratofim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoestadual)
        self.contratoinicio = contratoinicio
        self.contratofim = contratofim

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Contrato inicio: {self.contratoinicio}"
                f"\n Contrato fim: {self.contratofim}")
    
class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoestadual)
        self.produto = produto

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Produto: {self.produto}")
    
class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.crea = crea

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Crea: {self.crea}")
    
class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.crm = crm

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Crm: {self.crm}")
    
class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.oab = oab

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Oab: {self.oab}")
    
cliente1 = Cliente(3213, "Roberto", "3333-4444", "Roberto33@gmail.com", Endereco("Rua B", "44", "N/A", "324234", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.CASADO, "09/04/1977", 342445)
prestacaoservico1 = PrestacaoServico(6521, "Saulo", "9932-2532", "Saal@gmail.com", Endereco("Avenida P", "32", "N/A", "43242", "São Paulo", UnidadeFederativa.SAO_PAULO), "31233", "76553", "04/02/2024", "04/02/2026")
fornecedor1 = Fornecedor(2133, "Paula", "4354-5421", "Paula223@gmail.com", Endereco("Rua K", "1", "N/A", "42455", "Camaçari", UnidadeFederativa.BAHIA), "32123", "65466", "Placa de Video")
engenheiro1 = Engenheiro(6496, "Renata", "8892-4342", "Rere@gmail.com", Endereco("Rua U", "21", "N/A", "42343", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "09/08/1999", "432443", "93243", "2353", Setor.ENGENHARIA, 3213, "24443")
medico1 = Medico(4543, "Jonatas", "3242-4321", "Flajon@gmail.com", Endereco("Rua G", "32", "N/A", "4457", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO), Sexo.MASCULINO, EstadoCivil.CASADO, "15/01/1980", "92344", "23432", "8456", Setor.SAUDE, 5600, "5465")
advogado1 = Advogado(4345, "Maria", "6786-2136", "Mari@gmail.com", Endereco("Rua P", "12", "N/A", "32447", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SEPARADO, "28/11/1985", "42434", "67574", "3239", Setor.JURIDICO, 4560, "8723")

print(cliente1)
print(prestacaoservico1)
print(fornecedor1)
print(engenheiro1)
print(medico1)
print(advogado1)