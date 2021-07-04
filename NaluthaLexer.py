# Generated from Nalutha.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\7\13J\n\13\f\13\16\13M\13\13")
        buf.write("\3\f\6\fP\n\f\r\f\16\fQ\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\2\33\16\35\17\3\2\6\4\2C\\c|\6\2\62;")
        buf.write("C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2\\\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2")
        buf.write("\5\'\3\2\2\2\7)\3\2\2\2\t\62\3\2\2\2\138\3\2\2\2\r:\3")
        buf.write("\2\2\2\17<\3\2\2\2\21C\3\2\2\2\23E\3\2\2\2\25G\3\2\2\2")
        buf.write("\27O\3\2\2\2\31S\3\2\2\2\33V\3\2\2\2\35Z\3\2\2\2\37 \7")
        buf.write("R\2\2 !\7t\2\2!\"\7q\2\2\"#\7l\2\2#$\7g\2\2$%\7e\2\2%")
        buf.write("&\7v\2\2&\4\3\2\2\2\'(\7<\2\2(\6\3\2\2\2)*\7C\2\2*+\7")
        buf.write("r\2\2+,\7k\2\2,-\7\"\2\2-.\7p\2\2./\7c\2\2/\60\7o\2\2")
        buf.write("\60\61\7g\2\2\61\b\3\2\2\2\62\63\7O\2\2\63\64\7q\2\2\64")
        buf.write("\65\7f\2\2\65\66\7g\2\2\66\67\7n\2\2\67\n\3\2\2\289\7")
        buf.write("}\2\29\f\3\2\2\2:;\7\177\2\2;\16\3\2\2\2<=\7G\2\2=>\7")
        buf.write("p\2\2>?\7v\2\2?@\7k\2\2@A\7v\2\2AB\7{\2\2B\20\3\2\2\2")
        buf.write("CD\7]\2\2D\22\3\2\2\2EF\7_\2\2F\24\3\2\2\2GK\t\2\2\2H")
        buf.write("J\t\3\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\26")
        buf.write("\3\2\2\2MK\3\2\2\2NP\t\4\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2")
        buf.write("\2\2QR\3\2\2\2R\30\3\2\2\2ST\7^\2\2TU\7)\2\2U\32\3\2\2")
        buf.write("\2VW\t\5\2\2WX\3\2\2\2XY\b\16\2\2Y\34\3\2\2\2Z[\13\2\2")
        buf.write("\2[\36\3\2\2\2\5\2KQ\3\b\2\2")
        return buf.getvalue()


class NaluthaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    Id = 10
    Num = 11
    WS = 12
    ERRO = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Project'", "':'", "'Api name'", "'Model'", "'{'", "'}'", "'Entity'", 
            "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "Id", "Num", "WS", "ERRO" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "Id", "Num", "ESC_SEQ", "WS", "ERRO" ]

    grammarFileName = "Nalutha.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


