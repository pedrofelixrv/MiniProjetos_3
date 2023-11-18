from operator import attrgetter
from src.aluno.base.funcionario import Funcionario
from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.aluno.base.terceirizado import Terceirizado
from src.cliente.irh_service import IRHService


class RHService(IRHService):
    def __init__(self):
        self.funcionarios = {}

    def cadastrar(self, funcionario: Funcionario):
        nome = input(str("NOME: "))
        cpf = input(int("CPF: "))
        cargo = input(str("CARGO: "))

        if cpf in self.funcionarios:
            print(f"CPF {cpf} já cadastrado. Não é possível inserir funcionários com CPFs repetidos.")
            return

        if cargo == "PROF":
            funcionario = Professor(cpf, nome, input(str("CLASSE: ")))
        elif cargo == "STA":
            funcionario = STA(cpf, nome, input(int("NÍVEL: ")))
        elif cargo == "TERC":
            funcionario = Terceirizado(cpf, nome, input(bool("INSALUBRIDADE: 0 - FALSO, 1 - VERDADEIRO")))
        else:
            print("Cargo inválido. Insira PROF, STA ou TERC.")
            return

        self.funcionarios[cpf] = funcionario
        print(f"Funcionário {nome} cadastrado com sucesso.")

    def remover(self, cpf: str):
        if cpf in self.funcionarios:
            del self.funcionarios[cpf]
            print(f"Funcionário com CPF {cpf} removido com sucesso.")
        else:
            print(f"Funcionário com CPF {cpf} não encontrado. Não é possível remover.")

    def obterFuncionario(self, cpf: str):
        if cpf in self.funcionarios:
            return self.funcionarios[cpf]
        else:
            print(f"Funcionário com CPF {cpf} não encontrado.")
            return None

    def getFuncionarios(self):
        funcionarios_ordenados = sorted(self.funcionarios.values(), key=attrgetter('nome'))
        for funcionario in funcionarios_ordenados:
            print(f"{funcionario.nome} (CPF: {funcionario.cpf}, Cargo: {type(funcionario).__name__})")

    def getFuncionariosPorCategorias(self, tipo, cargo=None):
        cargo = input(str("CARGO: "))
        funcionarios_cargo = [funcionario for funcionario in self.funcionarios.values() if
                              isinstance(funcionario, globals()[cargo])]
        funcionarios_ordenados = sorted(funcionarios_cargo, key=attrgetter('nome'))
        for funcionario in funcionarios_ordenados:
            print(f"{funcionario.nome} (CPF: {funcionario.cpf})")

    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if funcionario:
            diarias_utilizadas = funcionario.receber_diarias(quantidade)
            if diarias_utilizadas > 0:
                print(f"{diarias_utilizadas} diárias pagas para {funcionario.nome} (CPF: {funcionario.cpf}).")

    def partilharLucros(self, valor: float):
        if not self.funcionarios:
            print("Não há funcionários para receber participação nos lucros.")
            return

        valor_por_funcionario = valor / len(self.funcionarios)
        for funcionario in self.funcionarios.values():
            funcionario.receber_participacao_lucros(valor_por_funcionario)

    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        return None

    def calcularFolhaDePagamento(self):
        if not self.funcionarios:
            print("Não há funcionários cadastrados para calcular a folha de pagamento.")
            return 0

        total_salarios = 0
        for funcionario in self.funcionarios.values():
            total_salarios += funcionario.calcular_salario()

        return total_salarios
