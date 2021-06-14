# Generated from Nalutha.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\64\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7)")
        buf.write("\n\7\f\7\16\7,\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\2\2\n")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\t\3\2\5\4\2C\\c|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\63\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\21\3\2\2\2\3\23\3\2\2\2\5\31\3\2\2\2\7 \3\2\2\2\t")
        buf.write("\"\3\2\2\2\13$\3\2\2\2\r&\3\2\2\2\17-\3\2\2\2\21\60\3")
        buf.write("\2\2\2\23\24\7O\2\2\24\25\7q\2\2\25\26\7f\2\2\26\27\7")
        buf.write("g\2\2\27\30\7n\2\2\30\4\3\2\2\2\31\32\7G\2\2\32\33\7p")
        buf.write("\2\2\33\34\7v\2\2\34\35\7k\2\2\35\36\7v\2\2\36\37\7{\2")
        buf.write("\2\37\6\3\2\2\2 !\7<\2\2!\b\3\2\2\2\"#\7}\2\2#\n\3\2\2")
        buf.write("\2$%\7\177\2\2%\f\3\2\2\2&*\t\2\2\2\')\t\3\2\2(\'\3\2")
        buf.write("\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\16\3\2\2\2,*\3\2\2")
        buf.write("\2-.\7^\2\2./\7)\2\2/\20\3\2\2\2\60\61\t\4\2\2\61\62\3")
        buf.write("\2\2\2\62\63\b\t\2\2\63\22\3\2\2\2\4\2*\3\b\2\2")
        return buf.getvalue()


class NaluthaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    Id = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Model'", "'Entity'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "Id", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "Id", "ESC_SEQ", 
                  "WS" ]

    grammarFileName = "Nalutha.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


