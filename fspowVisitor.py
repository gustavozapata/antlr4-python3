# Generated from fspow.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fspowParser import fspowParser
else:
    from fspowParser import fspowParser
import settings
from pathlib import Path
# This class defines a complete generic visitor for a parse tree produced by fspowParser.

class fspowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fspowParser#prog.
    def visitProg(self, ctx:fspowParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fspowParser#stat.
    def visitStat(self, ctx:fspowParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fspowParser#fcCreation.
    def visitFcCreation(self, ctx:fspowParser.FcCreationContext):
        fcID = ctx.getChild(0).getText()
        root = ctx.getChild(4).getText()
        path = Path(root[1:len(root)-1]) # extract string w/o quotes
        files = [ e for e in path.rglob("*") if e.is_file() ] # list comprehension
        settings.ListOfFCs[fcID] = files
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by fspowParser#fcCreationName.
    def visitFcCreationName(self, ctx:fspowParser.FcCreationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fspowParser#rootSpecifier.
    def visitRootSpecifier(self, ctx:fspowParser.RootSpecifierContext):
        return self.visitChildren(ctx)



del fspowParser