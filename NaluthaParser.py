# Generated from Nalutha.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\33")
        buf.write("\n\4\f\4\16\4\36\13\4\3\4\3\4\3\5\3\5\3\5\3\5\6\5&\n\5")
        buf.write("\r\5\16\5\'\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6")
        buf.write("\3\6\2\2\7\2\4\6\b\n\2\2\2\61\2\f\3\2\2\2\4\20\3\2\2\2")
        buf.write("\6\27\3\2\2\2\b!\3\2\2\2\n+\3\2\2\2\f\r\5\4\3\2\r\16\5")
        buf.write("\6\4\2\16\17\7\2\2\3\17\3\3\2\2\2\20\21\7\3\2\2\21\22")
        buf.write("\7\4\2\2\22\23\7\f\2\2\23\24\7\5\2\2\24\25\7\4\2\2\25")
        buf.write("\26\7\f\2\2\26\5\3\2\2\2\27\30\7\6\2\2\30\34\7\7\2\2\31")
        buf.write("\33\5\b\5\2\32\31\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2")
        buf.write("\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37 \7\b\2\2")
        buf.write(" \7\3\2\2\2!\"\7\t\2\2\"#\7\f\2\2#%\7\7\2\2$&\5\n\6\2")
        buf.write("%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2")
        buf.write(")*\7\b\2\2*\t\3\2\2\2+,\7\f\2\2,-\7\4\2\2-\61\7\f\2\2")
        buf.write("./\7\n\2\2/\60\7\r\2\2\60\62\7\13\2\2\61.\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\13\3\2\2\2\5\34\'\61")
        return buf.getvalue()


class NaluthaParser ( Parser ):

    grammarFileName = "Nalutha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Project'", "':'", "'Api name'", "'Model'", 
                     "'{'", "'}'", "'Entity'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Id", "Num", "WS", "ERRO" ]

    RULE_program = 0
    RULE_config = 1
    RULE_model = 2
    RULE_entity = 3
    RULE_field = 4

    ruleNames =  [ "program", "config", "model", "entity", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    Id=10
    Num=11
    WS=12
    ERRO=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def config(self):
            return self.getTypedRuleContext(NaluthaParser.ConfigContext,0)


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
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.config()
            self.state = 11
            self.model()
            self.state = 12
            self.match(NaluthaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConfigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.projectName = None # Token
            self.apiName = None # Token

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(NaluthaParser.Id)
            else:
                return self.getToken(NaluthaParser.Id, i)

        def getRuleIndex(self):
            return NaluthaParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig" ):
                return visitor.visitConfig(self)
            else:
                return visitor.visitChildren(self)




    def config(self):

        localctx = NaluthaParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_config)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(NaluthaParser.T__0)
            self.state = 15
            self.match(NaluthaParser.T__1)
            self.state = 16
            localctx.projectName = self.match(NaluthaParser.Id)
            self.state = 17
            self.match(NaluthaParser.T__2)
            self.state = 18
            self.match(NaluthaParser.T__1)
            self.state = 19
            localctx.apiName = self.match(NaluthaParser.Id)
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
        self.enterRule(localctx, 4, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(NaluthaParser.T__3)
            self.state = 22
            self.match(NaluthaParser.T__4)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NaluthaParser.T__6:
                self.state = 23
                self.entity()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(NaluthaParser.T__5)
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
        self.enterRule(localctx, 6, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NaluthaParser.T__6)
            self.state = 32
            self.match(NaluthaParser.Id)
            self.state = 33
            self.match(NaluthaParser.T__4)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.field()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NaluthaParser.Id):
                    break

            self.state = 39
            self.match(NaluthaParser.T__5)
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
            self.fieldSize = None # Token

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(NaluthaParser.Id)
            else:
                return self.getToken(NaluthaParser.Id, i)

        def Num(self):
            return self.getToken(NaluthaParser.Num, 0)

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
        self.enterRule(localctx, 8, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            localctx.fieldName = self.match(NaluthaParser.Id)
            self.state = 42
            self.match(NaluthaParser.T__1)
            self.state = 43
            localctx.fieldType = self.match(NaluthaParser.Id)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NaluthaParser.T__7:
                self.state = 44
                self.match(NaluthaParser.T__7)
                self.state = 45
                localctx.fieldSize = self.match(NaluthaParser.Num)
                self.state = 46
                self.match(NaluthaParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





