# Generated from BayesGrammarUser.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\fQ\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2")
        buf.write(u"\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write(u"\3\t\3\n\6\n+\n\n\r\n\16\n,\3\13\6\13\60\n\13\r\13\16")
        buf.write(u"\13\61\3\13\3\13\3\f\3\f\3\f\3\f\7\f:\n\f\f\f\16\f=\13")
        buf.write(u"\f\3\f\5\f@\n\f\3\f\3\f\3\f\3\f\3\f\7\fG\n\f\f\f\16\f")
        buf.write(u"J\13\f\3\f\3\f\5\fN\n\f\3\f\3\f\3H\2\r\3\3\5\4\7\5\t")
        buf.write(u"\6\13\7\r\b\17\2\21\t\23\n\25\13\27\f\3\2\5\4\2C\\c|")
        buf.write(u"\5\2\13\f\16\17\"\"\4\2\f\f\17\17U\2\3\3\2\2\2\2\5\3")
        buf.write(u"\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write(u"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write(u"\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2")
        buf.write(u"\2\13!\3\2\2\2\r#\3\2\2\2\17%\3\2\2\2\21\'\3\2\2\2\23")
        buf.write(u"*\3\2\2\2\25/\3\2\2\2\27M\3\2\2\2\31\32\7R\2\2\32\4\3")
        buf.write(u"\2\2\2\33\34\7r\2\2\34\6\3\2\2\2\35\36\7*\2\2\36\b\3")
        buf.write(u"\2\2\2\37 \7+\2\2 \n\3\2\2\2!\"\7~\2\2\"\f\3\2\2\2#$")
        buf.write(u"\7.\2\2$\16\3\2\2\2%&\t\2\2\2&\20\3\2\2\2\'(\7#\2\2(")
        buf.write(u"\22\3\2\2\2)+\5\17\b\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2")
        buf.write(u",-\3\2\2\2-\24\3\2\2\2.\60\t\3\2\2/.\3\2\2\2\60\61\3")
        buf.write(u"\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64")
        buf.write(u"\b\13\2\2\64\26\3\2\2\2\65\66\7\61\2\2\66\67\7\61\2\2")
        buf.write(u"\67;\3\2\2\28:\n\4\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2")
        buf.write(u";<\3\2\2\2<?\3\2\2\2=;\3\2\2\2>@\7\17\2\2?>\3\2\2\2?")
        buf.write(u"@\3\2\2\2@A\3\2\2\2AN\7\f\2\2BC\7\61\2\2CD\7,\2\2DH\3")
        buf.write(u"\2\2\2EG\13\2\2\2FE\3\2\2\2GJ\3\2\2\2HI\3\2\2\2HF\3\2")
        buf.write(u"\2\2IK\3\2\2\2JH\3\2\2\2KL\7,\2\2LN\7\61\2\2M\65\3\2")
        buf.write(u"\2\2MB\3\2\2\2NO\3\2\2\2OP\b\f\2\2P\30\3\2\2\2\t\2,\61")
        buf.write(u";?HM\3\b\2\2")
        return buf.getvalue()


class BayesGrammarUserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NEGATION = 7
    TOKEN = 8
    WS = 9
    COMMENT = 10

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'P'", u"'p'", u"'('", u"')'", u"'|'", u"','", u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"NEGATION", u"TOKEN", u"WS", u"COMMENT" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"LETTER", u"NEGATION", u"TOKEN", u"WS", u"COMMENT" ]

    grammarFileName = u"BayesGrammarUser.txt"

    def __init__(self, input=None):
        super(BayesGrammarUserLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


