from NaluthaVisitor import NaluthaVisitor
from NaluthaParser import NaluthaParser
from Escopo import Escopo
from MyVisitorSemanticoUtils import MyVisitorSemanticoUtils

class MyVisitorSemantico(NaluthaVisitor):
    def __init__(self):
        self.escopo = Escopo()

    def visitEntity(self, ctx):
        name = ctx.Id().getText()
        self.escopo.criarNovoEscopo()
        retorno = self.visitChildren(ctx)
        self.escopo.abandonarEscopo()
        return retorno

    def visitField(self, ctx):
        name = ctx.fieldName.text
        linha = str(ctx.fieldName.line)
        escopoAtual = self.escopo.obterEscopoAtual()

        if not escopoAtual.existe(name):
            escopoAtual.inserir(name)
        else:
            mensagem = ""+name+ "já está declarado"
            MyVisitorSemanticoUtils(ctx.start, mensagem)
        return self.visitChildren(ctx)