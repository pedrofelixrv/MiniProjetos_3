class Funcionario:

    def __init__(self, cpf: str, nome: str):
        self.cpf = cpf
        self.nome = nome

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        pass