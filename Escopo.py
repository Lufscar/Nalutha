from TabelaDeSimbolos import TabelaDeSimbolos 

class Escopo():
    def __init__(self):
        self.pilhaDeTabelas = []
        self.criarNovoEscopo()

    def criarNovoEscopo(self):
        self.pilhaDeTabelas.append(TabelaDeSimbolos())

    def obterEscopoAtual(self):
        return self.pilhaDeTabelas[-1]

    def percorrerEscoposAninhados(self):
        return self.pilhaDeTabelas

    def abandonarEscopo(self):
        return self.pilhaDeTabelas.pop()