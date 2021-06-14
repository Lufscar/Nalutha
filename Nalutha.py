from NaluthaLexer import NaluthaLexer
from NaluthaParser import NaluthaParser
from antlr4 import *
from MyVisitorSemantico import MyVisitorSemantico
from Saida import *
import sys

def main(argv):
    ipt = FileStream(argv[1])
    lexer = NaluthaLexer(ipt)
    stream = CommonTokenStream(lexer)
    parser = NaluthaParser(stream)
    tree = parser.program()
    visitor = MyVisitorSemantico()
    visitor.visit(tree)
    saida = self.saida
    generated = PrintWriter(argv[1])
    try:
    	generated.print(saida.toString())

if __name__ == '__main__':
	main(sys.argv)