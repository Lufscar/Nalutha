from antlr4 import Token

class MyVisitorSemanticoUtils():
    def __init__(self):
    # Inicializa a lista de erros semânticos
        self.errosSemanticos = []

    def adicionarErroSemantico(self, ctx, mensagem):
    # adiciona erro semântico na lista de erros
        linha = str(ctx.fieldName.line)
        self.errosSemanticos.append("Linha "+linha+": "+mensagem)
