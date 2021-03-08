import sys
from antlr4 import *
from fspowLexer import fspowLexer
from fspowParser import fspowParser
from fspowVisitor import fspowVisitor
# from fspowListener import fspowListener

from antlr4.tree.Trees import Trees

import settings
settings.init() 

def main(argv):
    if len(argv) == 1:
        inpstream = StdinStream()
    else:
        inpname = argv[1]
        inpstream = FileStream(inpname)

    lexer = fspowLexer(inpstream)
    tokstream = CommonTokenStream(lexer)
    parser = fspowParser(tokstream)

    tree = parser.prog()
    print(Trees.toStringTree(tree, None, parser))

    # Using listener
    # listener = fspowListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    # Using visitor
    visitor = fspowVisitor()
    visitor.visit(tree)

    print(settings.ListOfFCs)

if __name__ == '__main__':
    main(sys.argv)
