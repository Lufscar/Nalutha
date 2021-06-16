# Generated from Nalutha.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NaluthaParser import NaluthaParser
else:
    from NaluthaParser import NaluthaParser

# This class defines a complete generic visitor for a parse tree produced by NaluthaParser.

class NaluthaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NaluthaParser#model_lex.
    def visitModel_lex(self, ctx:NaluthaParser.Model_lexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#entity_lex.
    def visitEntity_lex(self, ctx:NaluthaParser.Entity_lexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#dois_pontos.
    def visitDois_pontos(self, ctx:NaluthaParser.Dois_pontosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#abre_chave.
    def visitAbre_chave(self, ctx:NaluthaParser.Abre_chaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#fecha_chave.
    def visitFecha_chave(self, ctx:NaluthaParser.Fecha_chaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#program.
    def visitProgram(self, ctx:NaluthaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#model.
    def visitModel(self, ctx:NaluthaParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#entity.
    def visitEntity(self, ctx:NaluthaParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#field.
    def visitField(self, ctx:NaluthaParser.FieldContext):
        return self.visitChildren(ctx)



del NaluthaParser