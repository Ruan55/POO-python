import os
os.system("cls || clear")

class ContaBancaria:
    def __init__(self, banco: str, agencia: str, numeroDeConta: str, tipoDeConta: str, saldoAtual: float, limiteDisponivel: str) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numerodeconta = numeroDeConta
        self.tipodeconta = tipoDeConta
        self.saldoatual = saldoAtual
        self.limitedisponivel = limiteDisponivel

    def __str__(self) -> str:
        return (f'\n Banco: {self.banco}'
                f'\n Agência: {self.agencia}'
                f'\n Numero de conta: {self.numerodeconta}'
                f'\n Tipo de conta: {self.tipodeconta}'
                f'\n Saldo atual: {self.saldoatual}'
                f'\n Limite disponivel: {self.limitedisponivel}')
    
class Funcionario:
    def __init__(self, codigoDoFuncionario: str, nome: str, endereco: str, telefone: str, email: str, contaBanco: ContaBancaria) -> None:
        self.codigodofuncionario = codigoDoFuncionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.contBanco = contaBanco

    def __str__(self) -> str:
        return (f'\n Código do Funcionário: {self.codigodofuncionario}'
                f'\n Nome: {self.nome}'
                f'\n Endereço: {self.endereco}'
                f'\n Telefone: {self.telefone}'
                f'\n E-mail: {self.email}'
                f'\n Conta banco: {self.contBanco}')
    
funcionario = Funcionario("3123sfs", "Ruan", "Rua A", "3232-6565", "Ruan323@gmail.com", ContaBancaria("Bradesco", "2133", "1232135", "013", 3213.65, "1600"))

print(funcionario)