from NaluthaLexer import NaluthaLexer
from NaluthaParser import NaluthaParser
from antlr4 import *
from MyVisitor import MyVisitor
import sys

def main(argv):
    ipt = FileStream(argv[1])
    lexer = NaluthaLexer(ipt)
    stream = CommonTokenStream(lexer)
    parser = NaluthaParser(stream)
    tree = parser.program()
    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)