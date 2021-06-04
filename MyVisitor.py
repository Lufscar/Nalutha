from NaluthaVisitor import NaluthaVisitor
from NaluthaParser import NaluthaParser
from Escopo import Escopo

class MyVisitor(NaluthaVisitor):
    def __init__(self):
        self.escopo = Escopo()

    def visitEntity(self, ctx):
        name = ctx.Id().getText()
        self.escopo.criarNovoEscopo()
        retorno = self.visitChildren(ctx)
        self.escopo.abandonarEscopo()
        return retorno

    def visitField(self, ctx):
        name = ctx.Id()[0].getText()
        linha = str(ctx.Id()[0].getSymbol().line)
        escopoAtual = self.escopo.obterEscopoAtual()

        if not escopoAtual.existe(name):
            escopoAtual.inserir(name)
        else:
            print("Erro " + linha + ": " + name + " já está declarado")

        return self.visitChildren(ctx)