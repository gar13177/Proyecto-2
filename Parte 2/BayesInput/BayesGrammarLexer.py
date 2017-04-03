# Generated from BayesGrammar.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\17a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4")
        buf.write(u"\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write(u"\3\13\3\13\3\f\3\f\3\r\6\r9\n\r\r\r\16\r:\3\16\3\16\3")
        buf.write(u"\17\6\17@\n\17\r\17\16\17A\3\17\3\17\3\20\3\20\3\20\3")
        buf.write(u"\20\7\20J\n\20\f\20\16\20M\13\20\3\20\5\20P\n\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\7\20W\n\20\f\20\16\20Z\13\20\3\20")
        buf.write(u"\3\20\5\20^\n\20\3\20\3\20\3X\2\21\3\3\5\4\7\5\t\6\13")
        buf.write(u"\7\r\b\17\t\21\n\23\2\25\2\27\13\31\f\33\r\35\16\37\17")
        buf.write(u"\3\2\5\4\2C\\c|\5\2\13\f\16\17\"\"\4\2\f\f\17\17d\2\3")
        buf.write(u"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write(u"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2")
        buf.write(u"\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write(u"\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3")
        buf.write(u"\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2")
        buf.write(u"\2\25\63\3\2\2\2\27\65\3\2\2\2\318\3\2\2\2\33<\3\2\2")
        buf.write(u"\2\35?\3\2\2\2\37]\3\2\2\2!\"\7R\2\2\"\4\3\2\2\2#$\7")
        buf.write(u"r\2\2$\6\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2(\n\3\2")
        buf.write(u"\2\2)*\7?\2\2*\f\3\2\2\2+,\7~\2\2,\16\3\2\2\2-.\7\60")
        buf.write(u"\2\2.\20\3\2\2\2/\60\7.\2\2\60\22\3\2\2\2\61\62\t\2\2")
        buf.write(u"\2\62\24\3\2\2\2\63\64\4\62;\2\64\26\3\2\2\2\65\66\7")
        buf.write(u"#\2\2\66\30\3\2\2\2\679\5\23\n\28\67\3\2\2\29:\3\2\2")
        buf.write(u"\2:8\3\2\2\2:;\3\2\2\2;\32\3\2\2\2<=\5\25\13\2=\34\3")
        buf.write(u"\2\2\2>@\t\3\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2")
        buf.write(u"\2\2BC\3\2\2\2CD\b\17\2\2D\36\3\2\2\2EF\7\61\2\2FG\7")
        buf.write(u"\61\2\2GK\3\2\2\2HJ\n\4\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2")
        buf.write(u"\2\2KL\3\2\2\2LO\3\2\2\2MK\3\2\2\2NP\7\17\2\2ON\3\2\2")
        buf.write(u"\2OP\3\2\2\2PQ\3\2\2\2Q^\7\f\2\2RS\7\61\2\2ST\7,\2\2")
        buf.write(u"TX\3\2\2\2UW\13\2\2\2VU\3\2\2\2WZ\3\2\2\2XY\3\2\2\2X")
        buf.write(u"V\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[\\\7,\2\2\\^\7\61\2\2]")
        buf.write(u"E\3\2\2\2]R\3\2\2\2^_\3\2\2\2_`\b\20\2\2` \3\2\2\2\t")
        buf.write(u"\2:AKOX]\3\b\2\2")
        return buf.getvalue()


class BayesGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NEGATION = 9
    TOKEN = 10
    NUMBERS = 11
    WS = 12
    COMMENT = 13

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'P'", u"'p'", u"'('", u"')'", u"'='", u"'|'", u"'.'", u"','", 
            u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"NEGATION", u"TOKEN", u"NUMBERS", u"WS", u"COMMENT" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"LETTER", u"NUMBER", u"NEGATION", u"TOKEN", 
                  u"NUMBERS", u"WS", u"COMMENT" ]

    grammarFileName = u"BayesGrammar.txt"

    def __init__(self, input=None):
        super(BayesGrammarLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


