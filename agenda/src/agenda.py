from contato import Contato
from identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.get_name())

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome: str) -> Contato:
        for contato in self.contatos:
            if contato.get_name() == nome:
                return contato
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if contato in self.contatos:
            contato.append(contato)
        else:
            novo_contato = Contato(contato)
            self.contatos.append(novo_contato)
        return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.get_name() == nome:
                self.contatos.remove(contato)
                return True
        return False

    def removerFone(self, nome: str, index: int) -> bool:
        contato = self.getContato(nome)
        if contato:
            return contato.removerFone(index)
        return False

    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        quantidade = 0
        for contato in self.contatos:
            for fone in contato.get_fones():
                if fone["identificador"] == identificador:
                    quantidade += 1
        return quantidade

    def pesquisar(self, expressao: str) -> list:
        resultados = []
        for contato in self.contatos:
            if expressao.lower() in contato.get_name().lower():
                resultados.append(contato)
        return resultados
