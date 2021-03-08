# Generated from fspow.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\6\6)\n")
        buf.write("\6\r\6\16\6*\3\7\3\7\7\7/\n\7\f\7\16\7\62\13\7\3\7\3\7")
        buf.write("\3\b\6\b\67\n\b\r\b\16\b8\3\b\3\b\3\60\2\t\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\3\2\5\4\2C\\c|\5\2\62;C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2>\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21")
        buf.write("\3\2\2\2\5\23\3\2\2\2\7\25\3\2\2\2\t\27\3\2\2\2\13&\3")
        buf.write("\2\2\2\r,\3\2\2\2\17\66\3\2\2\2\21\22\7?\2\2\22\4\3\2")
        buf.write("\2\2\23\24\7*\2\2\24\6\3\2\2\2\25\26\7+\2\2\26\b\3\2\2")
        buf.write("\2\27\30\7H\2\2\30\31\7k\2\2\31\32\7n\2\2\32\33\7g\2\2")
        buf.write("\33\34\7E\2\2\34\35\7q\2\2\35\36\7n\2\2\36\37\7n\2\2\37")
        buf.write(" \7g\2\2 !\7e\2\2!\"\7v\2\2\"#\7k\2\2#$\7q\2\2$%\7p\2")
        buf.write("\2%\n\3\2\2\2&(\t\2\2\2\')\t\3\2\2(\'\3\2\2\2)*\3\2\2")
        buf.write("\2*(\3\2\2\2*+\3\2\2\2+\f\3\2\2\2,\60\7$\2\2-/\13\2\2")
        buf.write("\2.-\3\2\2\2/\62\3\2\2\2\60\61\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\63\3\2\2\2\62\60\3\2\2\2\63\64\7$\2\2\64\16\3\2\2\2\65")
        buf.write("\67\t\4\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3")
        buf.write("\2\2\29:\3\2\2\2:;\b\b\2\2;\20\3\2\2\2\6\2*\608\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class fspowLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    STRING = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'FileCollection'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "STRING", "WS" ]

    grammarFileName = "fspow.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


