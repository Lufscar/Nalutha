# Generated from Nalutha.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NaluthaParser import NaluthaParser
else:
    from NaluthaParser import NaluthaParser

# This class defines a complete generic visitor for a parse tree produced by NaluthaParser.

class NaluthaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NaluthaParser#program.
    def visitProgram(self, ctx:NaluthaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NaluthaParser#config.
    def visitConfig(self, ctx:NaluthaParser.ConfigContext):
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