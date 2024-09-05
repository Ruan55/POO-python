from abc import ABC, abstractmethod
import os
os.system('cls || clear')

class Computador(ABC):
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def __str__(self) -> str:
        return (f'\n Marca: {self.marca}'
                f'\n Modelo: {self.modelo}')

class Processador(Computador):
    def __init__(self, marca: str, modelo: str, frequencia: str) -> None:
        super().__init__(marca, modelo)
        self.frequencia = frequencia

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Frequência: {self.frequencia}")
    
class Placamae(Computador):
    def __init__(self, marca: str, modelo: str, soquete: str) -> None:
        super().__init__(marca, modelo)
        self.soquete = soquete

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Soquete: {self.soquete}")
    
class Memoria(Computador):
    def __init__(self, marca: str, modelo: str, capacidadeDeArmazenamento: str, frequencia: str) -> None:
        super().__init__(marca, modelo)
        self.capacidaDeArmazenamento = capacidadeDeArmazenamento
        self.frequencia = frequencia

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Capacidade de armazenamento: {self.capacidaDeArmazenamento}"
                f"\n Frequência: {self.frequencia}")
    
class DispositivoDeArmazenamento(Computador):
    def __init__(self, marca: str, modelo: str, capacidadeArmazenamento: str, tipoDeConexao: str) -> None:
        super().__init__(marca, modelo)
        self.capacidadeArmazenamento = capacidadeArmazenamento
        self.tipoConexao = tipoDeConexao

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Capacidade armazenamento: {self.capacidadeArmazenamento}"
                f"\n Tipo de conexão: {self.tipoConexao}")

processador1 = Processador("AMD", "Ryzen 5600", "3.5 GHz")
placamae1 = Placamae("ASUS", "A520M-E", "AMD AM4")
memoria1 = Memoria("Corsair", "VENGEANCE LPX", "16GB", "3200mhz")
dispositivodearmazenamento1 = DispositivoDeArmazenamento("Seagate", "BarraCuda", "1TB", "SATA")

print(f"Processador: {processador1}")
print(f"Placa mãe: {placamae1}")
print(f"Mémoria: {memoria1}")
print(f"Dispositivo Armazenamento: {dispositivodearmazenamento1}")