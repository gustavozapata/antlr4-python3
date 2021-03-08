# Generated from fspow.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fspowParser import fspowParser
else:
    from fspowParser import fspowParser

# This class defines a complete listener for a parse tree produced by fspowParser.
class fspowListener(ParseTreeListener):

    # Enter a parse tree produced by fspowParser#prog.
    def enterProg(self, ctx:fspowParser.ProgContext):
        pass

    # Exit a parse tree produced by fspowParser#prog.
    def exitProg(self, ctx:fspowParser.ProgContext):
        pass


    # Enter a parse tree produced by fspowParser#stat.
    def enterStat(self, ctx:fspowParser.StatContext):
        pass

    # Exit a parse tree produced by fspowParser#stat.
    def exitStat(self, ctx:fspowParser.StatContext):
        pass


    # Enter a parse tree produced by fspowParser#fcCreation.
    def enterFcCreation(self, ctx:fspowParser.FcCreationContext):
        pass

    # Exit a parse tree produced by fspowParser#fcCreation.
    def exitFcCreation(self, ctx:fspowParser.FcCreationContext):
        pass


    # Enter a parse tree produced by fspowParser#fcCreationName.
    def enterFcCreationName(self, ctx:fspowParser.FcCreationNameContext):
        pass

    # Exit a parse tree produced by fspowParser#fcCreationName.
    def exitFcCreationName(self, ctx:fspowParser.FcCreationNameContext):
        pass


    # Enter a parse tree produced by fspowParser#rootSpecifier.
    def enterRootSpecifier(self, ctx:fspowParser.RootSpecifierContext):
        pass

    # Exit a parse tree produced by fspowParser#rootSpecifier.
    def exitRootSpecifier(self, ctx:fspowParser.RootSpecifierContext):
        pass



del fspowParser