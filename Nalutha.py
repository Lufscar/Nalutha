from NaluthaLexer import NaluthaLexer
from NaluthaParser import NaluthaParser
from antlr4 import *
from MyVisitorSemantico import MyVisitorSemantico
from MyVisitorGerador import MyVisitorGerador
import sys

def main(argv):
    ipt = FileStream(argv[1])
    lexer = NaluthaLexer(ipt)
    stream = CommonTokenStream(lexer)
    parser = NaluthaParser(stream)
    tree = parser.program()
    if semantico(tree):
        visitorGerador = MyVisitorGerador(argv[2])
        visitorGerador.visit(tree)
    else:
        print("Falha na criação do arquivo de saída.")


def semantico(tree):
    visitorSemantico = MyVisitorSemantico()
    visitorSemantico.visit(tree)
    for error in visitorSemantico.semanticoUtils.errosSemanticos:
        print(error)
    if not visitorSemantico.semanticoUtils.errosSemanticos: # list is empty
        return True
    return False


if __name__ == '__main__':
    main(sys.argv)