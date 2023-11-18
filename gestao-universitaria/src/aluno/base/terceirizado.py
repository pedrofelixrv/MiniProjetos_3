from src.aluno.base.funcionario import Funcionario


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        super().__init__(cpf, nome)
        self.insalubre = insalubre
