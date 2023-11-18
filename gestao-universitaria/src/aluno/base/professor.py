from src.aluno.base.funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        def __init__(self, cpf: str, nome: str, classe: str):
            super().__init__(cpf, nome)
            self.classe = classe
