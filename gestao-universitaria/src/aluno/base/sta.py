from src.aluno.base.funcionario import Funcionario


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        super().__init__(cpf, nome)
        self.nivel = nivel
