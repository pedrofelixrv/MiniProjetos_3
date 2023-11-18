from src.fone import Fone


class Contato:

    def __init__(self, nome):
        self.nome = nome
        self.fones = []

    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        return len(self.fones)

    def getFones(self) -> list:
        return self.fones

    def adicionarFone(self, fone: Fone) -> bool:
        if not fone.validarNumero(Fone):
            return False

        novo_fone = {fone: Fone}
        self.fones.append(novo_fone)
        return True

    def removerFone(self, index: int) -> bool:
        if 0 <= index < len(self.fones):
            del self.fones[index]
            return True
        else:
            return False
