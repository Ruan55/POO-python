import os
os.system("cls || clear")

# Criando minha própria exceção.
class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

    # Semelhante ao getSaldo()
    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        try:
            self.__verificar_valor_negativo(valor_saque)
        except ValorNegativoError as erro:
            return f"Erro: {erro}"
        try:
            self.__verificar_sacar(valor_saque)
        except SaldoInsuficienteError as erro:
            return f"Erro: {erro}"

        return f"Saque realizado com sucesso."

    # Método privado
    def __verificar_sacar(self, valor) -> float:
        if valor >= self._saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente!")
        
        self._saldo -= valor

    def __verificar_valor_negativo(self, valor):
        if valor < self._saldo:
            raise ValorNegativoError("Saldo Negativo!")
        

    def depositar(self):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        try:
            self.__verificar_valor_negativo(valor_deposito)
        except ValorNegativoError as erro:
            return f"Prezado cliente: {erro}"

        return "Deposito realizado com sucesso"

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# Instanciando classe.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

print(f"Saldo: {conta_corrente.saldo}")
print(f"Número da conta: {conta_corrente.numero_conta}")

print(conta_corrente.sacar())
print(conta_poupanca.sacar())
print(conta_corrente.depositar())
print(conta_poupanca.depositar())