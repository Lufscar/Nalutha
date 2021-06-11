from Simbolos import Simbolos

class TabelaDeSimbolos():
    def __init__(self):
        self.tabela = {}

    def inserir(self, field):
        self.tabela[field] = Simbolos(field)

    def existe(self, field):
        if field not in self.tabela: 
            return False
        return True