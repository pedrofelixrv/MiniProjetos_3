from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        caracteres_permitidos = set("0123456789()-")
        return all(caractere in caracteres_permitidos for caractere in numero)

    def getIdentificador(self) -> Identificador:
        return Identificador.CASA

    def getNumero(self) -> str:
        return self.numero
