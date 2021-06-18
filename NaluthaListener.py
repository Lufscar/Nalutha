# Generated from Nalutha.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NaluthaParser import NaluthaParser
else:
    from NaluthaParser import NaluthaParser

# This class defines a complete listener for a parse tree produced by NaluthaParser.
class NaluthaListener(ParseTreeListener):

    # Enter a parse tree produced by NaluthaParser#program.
    def enterProgram(self, ctx:NaluthaParser.ProgramContext):
        pass

    # Exit a parse tree produced by NaluthaParser#program.
    def exitProgram(self, ctx:NaluthaParser.ProgramContext):
        pass


    # Enter a parse tree produced by NaluthaParser#config.
    def enterConfig(self, ctx:NaluthaParser.ConfigContext):
        pass

    # Exit a parse tree produced by NaluthaParser#config.
    def exitConfig(self, ctx:NaluthaParser.ConfigContext):
        pass


    # Enter a parse tree produced by NaluthaParser#model.
    def enterModel(self, ctx:NaluthaParser.ModelContext):
        pass

    # Exit a parse tree produced by NaluthaParser#model.
    def exitModel(self, ctx:NaluthaParser.ModelContext):
        pass


    # Enter a parse tree produced by NaluthaParser#entity.
    def enterEntity(self, ctx:NaluthaParser.EntityContext):
        pass

    # Exit a parse tree produced by NaluthaParser#entity.
    def exitEntity(self, ctx:NaluthaParser.EntityContext):
        pass


    # Enter a parse tree produced by NaluthaParser#field.
    def enterField(self, ctx:NaluthaParser.FieldContext):
        pass

    # Exit a parse tree produced by NaluthaParser#field.
    def exitField(self, ctx:NaluthaParser.FieldContext):
        pass


