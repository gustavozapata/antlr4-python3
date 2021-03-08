# Generated from fspow.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\32\2\r\3\2\2")
        buf.write("\2\4\21\3\2\2\2\6\23\3\2\2\2\b\32\3\2\2\2\n\34\3\2\2\2")
        buf.write("\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17")
        buf.write("\20\3\2\2\2\20\3\3\2\2\2\21\22\5\6\4\2\22\5\3\2\2\2\23")
        buf.write("\24\7\7\2\2\24\25\7\3\2\2\25\26\5\b\5\2\26\27\7\4\2\2")
        buf.write("\27\30\5\n\6\2\30\31\7\5\2\2\31\7\3\2\2\2\32\33\7\6\2")
        buf.write("\2\33\t\3\2\2\2\34\35\7\b\2\2\35\13\3\2\2\2\3\17")
        return buf.getvalue()


class fspowParser ( Parser ):

    grammarFileName = "fspow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'FileCollection'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_fcCreation = 2
    RULE_fcCreationName = 3
    RULE_rootSpecifier = 4

    ruleNames =  [ "prog", "stat", "fcCreation", "fcCreationName", "rootSpecifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    STRING=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fspowParser.StatContext)
            else:
                return self.getTypedRuleContext(fspowParser.StatContext,i)


        def getRuleIndex(self):
            return fspowParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = fspowParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fspowParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fcCreation(self):
            return self.getTypedRuleContext(fspowParser.FcCreationContext,0)


        def getRuleIndex(self):
            return fspowParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = fspowParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.fcCreation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FcCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(fspowParser.ID, 0)

        def fcCreationName(self):
            return self.getTypedRuleContext(fspowParser.FcCreationNameContext,0)


        def rootSpecifier(self):
            return self.getTypedRuleContext(fspowParser.RootSpecifierContext,0)


        def getRuleIndex(self):
            return fspowParser.RULE_fcCreation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFcCreation" ):
                listener.enterFcCreation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFcCreation" ):
                listener.exitFcCreation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFcCreation" ):
                return visitor.visitFcCreation(self)
            else:
                return visitor.visitChildren(self)




    def fcCreation(self):

        localctx = fspowParser.FcCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fcCreation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(fspowParser.ID)
            self.state = 18
            self.match(fspowParser.T__0)
            self.state = 19
            self.fcCreationName()
            self.state = 20
            self.match(fspowParser.T__1)
            self.state = 21
            self.rootSpecifier()
            self.state = 22
            self.match(fspowParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FcCreationNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fspowParser.RULE_fcCreationName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFcCreationName" ):
                listener.enterFcCreationName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFcCreationName" ):
                listener.exitFcCreationName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFcCreationName" ):
                return visitor.visitFcCreationName(self)
            else:
                return visitor.visitChildren(self)




    def fcCreationName(self):

        localctx = fspowParser.FcCreationNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fcCreationName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(fspowParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(fspowParser.STRING, 0)

        def getRuleIndex(self):
            return fspowParser.RULE_rootSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootSpecifier" ):
                listener.enterRootSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootSpecifier" ):
                listener.exitRootSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRootSpecifier" ):
                return visitor.visitRootSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def rootSpecifier(self):

        localctx = fspowParser.RootSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rootSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(fspowParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





