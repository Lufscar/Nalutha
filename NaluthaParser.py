# Generated from Nalutha.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b%\n\b\f\b\16\b(\13\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\6\t\60\n\t\r\t\16\t\61\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2")
        buf.write("\2\62\2\24\3\2\2\2\4\26\3\2\2\2\6\30\3\2\2\2\b\32\3\2")
        buf.write("\2\2\n\34\3\2\2\2\f\36\3\2\2\2\16!\3\2\2\2\20+\3\2\2\2")
        buf.write("\22\65\3\2\2\2\24\25\7\3\2\2\25\3\3\2\2\2\26\27\7\4\2")
        buf.write("\2\27\5\3\2\2\2\30\31\7\5\2\2\31\7\3\2\2\2\32\33\7\6\2")
        buf.write("\2\33\t\3\2\2\2\34\35\7\7\2\2\35\13\3\2\2\2\36\37\5\16")
        buf.write("\b\2\37 \7\2\2\3 \r\3\2\2\2!\"\7\3\2\2\"&\7\6\2\2#%\5")
        buf.write("\20\t\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3")
        buf.write("\2\2\2(&\3\2\2\2)*\7\7\2\2*\17\3\2\2\2+,\7\4\2\2,-\7\b")
        buf.write("\2\2-/\7\6\2\2.\60\5\22\n\2/.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64\7\7\2\2\64")
        buf.write("\21\3\2\2\2\65\66\7\b\2\2\66\67\7\5\2\2\678\7\b\2\28\23")
        buf.write("\3\2\2\2\4&\61")
        return buf.getvalue()


class NaluthaParser ( Parser ):

    grammarFileName = "Nalutha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Model'", "'Entity'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Id", "WS" ]

    RULE_model_lex = 0
    RULE_entity_lex = 1
    RULE_dois_pontos = 2
    RULE_abre_chave = 3
    RULE_fecha_chave = 4
    RULE_program = 5
    RULE_model = 6
    RULE_entity = 7
    RULE_field = 8

    ruleNames =  [ "model_lex", "entity_lex", "dois_pontos", "abre_chave", 
                   "fecha_chave", "program", "model", "entity", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Id=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Model_lexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NaluthaParser.RULE_model_lex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_lex" ):
                listener.enterModel_lex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_lex" ):
                listener.exitModel_lex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel_lex" ):
                return visitor.visitModel_lex(self)
            else:
                return visitor.visitChildren(self)




    def model_lex(self):

        localctx = NaluthaParser.Model_lexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_model_lex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(NaluthaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Entity_lexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NaluthaParser.RULE_entity_lex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_lex" ):
                listener.enterEntity_lex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_lex" ):
                listener.exitEntity_lex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_lex" ):
                return visitor.visitEntity_lex(self)
            else:
                return visitor.visitChildren(self)




    def entity_lex(self):

        localctx = NaluthaParser.Entity_lexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entity_lex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(NaluthaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dois_pontosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NaluthaParser.RULE_dois_pontos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDois_pontos" ):
                listener.enterDois_pontos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDois_pontos" ):
                listener.exitDois_pontos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDois_pontos" ):
                return visitor.visitDois_pontos(self)
            else:
                return visitor.visitChildren(self)




    def dois_pontos(self):

        localctx = NaluthaParser.Dois_pontosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dois_pontos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(NaluthaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abre_chaveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NaluthaParser.RULE_abre_chave

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbre_chave" ):
                listener.enterAbre_chave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbre_chave" ):
                listener.exitAbre_chave(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbre_chave" ):
                return visitor.visitAbre_chave(self)
            else:
                return visitor.visitChildren(self)




    def abre_chave(self):

        localctx = NaluthaParser.Abre_chaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_abre_chave)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(NaluthaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fecha_chaveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NaluthaParser.RULE_fecha_chave

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFecha_chave" ):
                listener.enterFecha_chave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFecha_chave" ):
                listener.exitFecha_chave(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFecha_chave" ):
                return visitor.visitFecha_chave(self)
            else:
                return visitor.visitChildren(self)




    def fecha_chave(self):

        localctx = NaluthaParser.Fecha_chaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fecha_chave)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(NaluthaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self):
            return self.getTypedRuleContext(NaluthaParser.ModelContext,0)


        def EOF(self):
            return self.getToken(NaluthaParser.EOF, 0)

        def getRuleIndex(self):
            return NaluthaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NaluthaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.model()
            self.state = 29
            self.match(NaluthaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NaluthaParser.EntityContext)
            else:
                return self.getTypedRuleContext(NaluthaParser.EntityContext,i)


        def getRuleIndex(self):
            return NaluthaParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = NaluthaParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NaluthaParser.T__0)
            self.state = 32
            self.match(NaluthaParser.T__3)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NaluthaParser.T__1:
                self.state = 33
                self.entity()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(NaluthaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(NaluthaParser.Id, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NaluthaParser.FieldContext)
            else:
                return self.getTypedRuleContext(NaluthaParser.FieldContext,i)


        def getRuleIndex(self):
            return NaluthaParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity" ):
                return visitor.visitEntity(self)
            else:
                return visitor.visitChildren(self)




    def entity(self):

        localctx = NaluthaParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(NaluthaParser.T__1)
            self.state = 42
            self.match(NaluthaParser.Id)
            self.state = 43
            self.match(NaluthaParser.T__3)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.field()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NaluthaParser.Id):
                    break

            self.state = 49
            self.match(NaluthaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fieldName = None # Token
            self.fieldType = None # Token

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(NaluthaParser.Id)
            else:
                return self.getToken(NaluthaParser.Id, i)

        def getRuleIndex(self):
            return NaluthaParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = NaluthaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            localctx.fieldName = self.match(NaluthaParser.Id)
            self.state = 52
            self.match(NaluthaParser.T__2)
            self.state = 53
            localctx.fieldType = self.match(NaluthaParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





