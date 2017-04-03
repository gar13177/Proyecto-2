# Generated from BayesGrammarUser.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\f,\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write(u"\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\5\3\5\3\6\5\6 \n\6\3\6\3\6\3\7\3\7\3\7\7\7\'\n")
        buf.write(u"\7\f\7\16\7*\13\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\3\4(")
        buf.write(u"\2\16\3\2\2\2\4\20\3\2\2\2\6\32\3\2\2\2\b\34\3\2\2\2")
        buf.write(u"\n\37\3\2\2\2\f#\3\2\2\2\16\17\5\4\3\2\17\3\3\2\2\2\20")
        buf.write(u"\21\t\2\2\2\21\22\7\5\2\2\22\26\5\f\7\2\23\24\5\6\4\2")
        buf.write(u"\24\25\5\f\7\2\25\27\3\2\2\2\26\23\3\2\2\2\26\27\3\2")
        buf.write(u"\2\2\27\30\3\2\2\2\30\31\7\6\2\2\31\5\3\2\2\2\32\33\7")
        buf.write(u"\7\2\2\33\7\3\2\2\2\34\35\7\t\2\2\35\t\3\2\2\2\36 \5")
        buf.write(u"\b\5\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\n\2\2")
        buf.write(u"\"\13\3\2\2\2#(\5\n\6\2$%\7\b\2\2%\'\5\n\6\2&$\3\2\2")
        buf.write(u"\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\r\3\2\2\2*(\3\2\2")
        buf.write(u"\2\5\26\37(")
        return buf.getvalue()


class BayesGrammarUserParser ( Parser ):

    grammarFileName = "BayesGrammarUser.txt"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'P'", u"'p'", u"'('", u"')'", u"'|'", 
                     u"','", u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"NEGATION", 
                      u"TOKEN", u"WS", u"COMMENT" ]

    RULE_program = 0
    RULE_probability = 1
    RULE_condition = 2
    RULE_negation = 3
    RULE_operator = 4
    RULE_op = 5

    ruleNames =  [ u"program", u"probability", u"condition", u"negation", 
                   u"operator", u"op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NEGATION=7
    TOKEN=8
    WS=9
    COMMENT=10

    def __init__(self, input):
        super(BayesGrammarUserParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def probability(self):
            return self.getTypedRuleContext(BayesGrammarUserParser.ProbabilityContext,0)


        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_program

        def enterRule(self, listener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)




    def program(self):

        localctx = BayesGrammarUserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.probability()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProbabilityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.ProbabilityContext, self).__init__(parent, invokingState)
            self.parser = parser

        def op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BayesGrammarUserParser.OpContext)
            else:
                return self.getTypedRuleContext(BayesGrammarUserParser.OpContext,i)


        def condition(self):
            return self.getTypedRuleContext(BayesGrammarUserParser.ConditionContext,0)


        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_probability

        def enterRule(self, listener):
            if hasattr(listener, "enterProbability"):
                listener.enterProbability(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProbability"):
                listener.exitProbability(self)




    def probability(self):

        localctx = BayesGrammarUserParser.ProbabilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_probability)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            _la = self._input.LA(1)
            if not(_la==BayesGrammarUserParser.T__0 or _la==BayesGrammarUserParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 15
            self.match(BayesGrammarUserParser.T__2)
            self.state = 16
            self.op()
            self.state = 20
            _la = self._input.LA(1)
            if _la==BayesGrammarUserParser.T__4:
                self.state = 17
                self.condition()
                self.state = 18
                self.op()


            self.state = 22
            self.match(BayesGrammarUserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.ConditionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_condition

        def enterRule(self, listener):
            if hasattr(listener, "enterCondition"):
                listener.enterCondition(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCondition"):
                listener.exitCondition(self)




    def condition(self):

        localctx = BayesGrammarUserParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(BayesGrammarUserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NegationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.NegationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NEGATION(self):
            return self.getToken(BayesGrammarUserParser.NEGATION, 0)

        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_negation

        def enterRule(self, listener):
            if hasattr(listener, "enterNegation"):
                listener.enterNegation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNegation"):
                listener.exitNegation(self)




    def negation(self):

        localctx = BayesGrammarUserParser.NegationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_negation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(BayesGrammarUserParser.NEGATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TOKEN(self):
            return self.getToken(BayesGrammarUserParser.TOKEN, 0)

        def negation(self):
            return self.getTypedRuleContext(BayesGrammarUserParser.NegationContext,0)


        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_operator

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator"):
                listener.enterOperator(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator"):
                listener.exitOperator(self)




    def operator(self):

        localctx = BayesGrammarUserParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if _la==BayesGrammarUserParser.NEGATION:
                self.state = 28
                self.negation()


            self.state = 31
            self.match(BayesGrammarUserParser.TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarUserParser.OpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def operator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BayesGrammarUserParser.OperatorContext)
            else:
                return self.getTypedRuleContext(BayesGrammarUserParser.OperatorContext,i)


        def getRuleIndex(self):
            return BayesGrammarUserParser.RULE_op

        def enterRule(self, listener):
            if hasattr(listener, "enterOp"):
                listener.enterOp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOp"):
                listener.exitOp(self)




    def op(self):

        localctx = BayesGrammarUserParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.operator()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BayesGrammarUserParser.T__5:
                self.state = 34
                self.match(BayesGrammarUserParser.T__5)
                self.state = 35
                self.operator()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





