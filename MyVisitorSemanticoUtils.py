from antlr4 import Token

class MyVisitorSemanticoUtils():
    def __init__(self):
    # Inicializa a lista de erros semânticos
        self.errosSemanticos = []

    def adicionarErroSemantico(self, t: Token, mensagem: str):
    # adiciona erro semântico na lista de erros
        linha = t.getLine()
        self.errosSemanticos.append("Linha "+linha+": "+mensagem)
