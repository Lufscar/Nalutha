from NaluthaLexer import NaluthaLexer
from NaluthaParser import NaluthaParser
from antlr4 import *
from MyVisitorSemantico import MyVisitorSemantico
from MyVisitorGerador import MyVisitorGerador
import sys
import antlr4

def main(argv):
    ipt = FileStream(argv[1])
    lexer = NaluthaLexer(ipt)
    stream = CommonTokenStream(lexer)
    parser = NaluthaParser(stream)
    tree = parser.program()
    visitorSemantico = MyVisitorSemantico()
    visitorSemantico.visit(tree)

    for error in visitorSemantico.semanticoUtils.errosSemanticos:
        print(error)

    if not visitorSemantico.semanticoUtils.errosSemanticos and not parser.getNumberOfSyntaxErrors(): # list is empty
        visitorGerador = MyVisitorGerador(argv[2])
        visitorGerador.visit(tree)


if __name__ == '__main__':
    main(sys.argv)