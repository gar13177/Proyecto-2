# Generated from BayesGrammar.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\17@\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\5\3\34\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write(u"\5\6\'\n\6\3\6\3\6\3\7\6\7,\n\7\r\7\16\7-\3\7\3\7\6\7")
        buf.write(u"\62\n\7\r\7\16\7\63\5\7\66\n\7\3\b\3\b\3\b\7\b;\n\b\f")
        buf.write(u"\b\16\b>\13\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\3\4?\2")
        buf.write(u"\21\3\2\2\2\4\25\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2\n&\3\2")
        buf.write(u"\2\2\f+\3\2\2\2\16\67\3\2\2\2\20\22\5\4\3\2\21\20\3\2")
        buf.write(u"\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3")
        buf.write(u"\2\2\2\25\26\t\2\2\2\26\27\7\5\2\2\27\33\5\16\b\2\30")
        buf.write(u"\31\5\6\4\2\31\32\5\16\b\2\32\34\3\2\2\2\33\30\3\2\2")
        buf.write(u"\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\7\6\2\2\36\37\7")
        buf.write(u"\7\2\2\37 \5\f\7\2 \5\3\2\2\2!\"\7\b\2\2\"\7\3\2\2\2")
        buf.write(u"#$\7\13\2\2$\t\3\2\2\2%\'\5\b\5\2&%\3\2\2\2&\'\3\2\2")
        buf.write(u"\2\'(\3\2\2\2()\7\f\2\2)\13\3\2\2\2*,\7\r\2\2+*\3\2\2")
        buf.write(u"\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\65\3\2\2\2/\61\7\t")
        buf.write(u"\2\2\60\62\7\r\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61")
        buf.write(u"\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65/\3\2\2\2\65\66")
        buf.write(u"\3\2\2\2\66\r\3\2\2\2\67<\5\n\6\289\7\n\2\29;\5\n\6\2")
        buf.write(u":8\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\17\3\2\2\2")
        buf.write(u"><\3\2\2\2\t\23\33&-\63\65<")
        return buf.getvalue()


class BayesGrammarParser ( Parser ):

    grammarFileName = "BayesGrammar.txt"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'P'", u"'p'", u"'('", u"')'", u"'='", 
                     u"'|'", u"'.'", u"','", u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"NEGATION", u"TOKEN", u"NUMBERS", u"WS", 
                      u"COMMENT" ]

    RULE_program = 0
    RULE_probability = 1
    RULE_condition = 2
    RULE_negation = 3
    RULE_operator = 4
    RULE_number = 5
    RULE_op = 6

    ruleNames =  [ u"program", u"probability", u"condition", u"negation", 
                   u"operator", u"number", u"op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NEGATION=9
    TOKEN=10
    NUMBERS=11
    WS=12
    COMMENT=13

    def __init__(self, input):
        super(BayesGrammarParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def probability(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BayesGrammarParser.ProbabilityContext)
            else:
                return self.getTypedRuleContext(BayesGrammarParser.ProbabilityContext,i)


        def getRuleIndex(self):
            return BayesGrammarParser.RULE_program

        def enterRule(self, listener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)




    def program(self):

        localctx = BayesGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.probability()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BayesGrammarParser.T__0 or _la==BayesGrammarParser.T__1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProbabilityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.ProbabilityContext, self).__init__(parent, invokingState)
            self.parser = parser

        def op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BayesGrammarParser.OpContext)
            else:
                return self.getTypedRuleContext(BayesGrammarParser.OpContext,i)


        def number(self):
            return self.getTypedRuleContext(BayesGrammarParser.NumberContext,0)


        def condition(self):
            return self.getTypedRuleContext(BayesGrammarParser.ConditionContext,0)


        def getRuleIndex(self):
            return BayesGrammarParser.RULE_probability

        def enterRule(self, listener):
            if hasattr(listener, "enterProbability"):
                listener.enterProbability(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProbability"):
                listener.exitProbability(self)




    def probability(self):

        localctx = BayesGrammarParser.ProbabilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_probability)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            _la = self._input.LA(1)
            if not(_la==BayesGrammarParser.T__0 or _la==BayesGrammarParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 20
            self.match(BayesGrammarParser.T__2)
            self.state = 21
            self.op()
            self.state = 25
            _la = self._input.LA(1)
            if _la==BayesGrammarParser.T__5:
                self.state = 22
                self.condition()
                self.state = 23
                self.op()


            self.state = 27
            self.match(BayesGrammarParser.T__3)
            self.state = 28
            self.match(BayesGrammarParser.T__4)
            self.state = 29
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.ConditionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BayesGrammarParser.RULE_condition

        def enterRule(self, listener):
            if hasattr(listener, "enterCondition"):
                listener.enterCondition(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCondition"):
                listener.exitCondition(self)




    def condition(self):

        localctx = BayesGrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(BayesGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NegationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.NegationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NEGATION(self):
            return self.getToken(BayesGrammarParser.NEGATION, 0)

        def getRuleIndex(self):
            return BayesGrammarParser.RULE_negation

        def enterRule(self, listener):
            if hasattr(listener, "enterNegation"):
                listener.enterNegation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNegation"):
                listener.exitNegation(self)




    def negation(self):

        localctx = BayesGrammarParser.NegationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_negation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(BayesGrammarParser.NEGATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TOKEN(self):
            return self.getToken(BayesGrammarParser.TOKEN, 0)

        def negation(self):
            return self.getTypedRuleContext(BayesGrammarParser.NegationContext,0)


        def getRuleIndex(self):
            return BayesGrammarParser.RULE_operator

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator"):
                listener.enterOperator(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator"):
                listener.exitOperator(self)




    def operator(self):

        localctx = BayesGrammarParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if _la==BayesGrammarParser.NEGATION:
                self.state = 35
                self.negation()


            self.state = 38
            self.match(BayesGrammarParser.TOKEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self, i=None):
            if i is None:
                return self.getTokens(BayesGrammarParser.NUMBERS)
            else:
                return self.getToken(BayesGrammarParser.NUMBERS, i)

        def getRuleIndex(self):
            return BayesGrammarParser.RULE_number

        def enterRule(self, listener):
            if hasattr(listener, "enterNumber"):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumber"):
                listener.exitNumber(self)




    def number(self):

        localctx = BayesGrammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(BayesGrammarParser.NUMBERS)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BayesGrammarParser.NUMBERS):
                    break

            self.state = 51
            _la = self._input.LA(1)
            if _la==BayesGrammarParser.T__6:
                self.state = 45
                self.match(BayesGrammarParser.T__6)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 46
                    self.match(BayesGrammarParser.NUMBERS)
                    self.state = 49 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BayesGrammarParser.NUMBERS):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BayesGrammarParser.OpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def operator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BayesGrammarParser.OperatorContext)
            else:
                return self.getTypedRuleContext(BayesGrammarParser.OperatorContext,i)


        def getRuleIndex(self):
            return BayesGrammarParser.RULE_op

        def enterRule(self, listener):
            if hasattr(listener, "enterOp"):
                listener.enterOp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOp"):
                listener.exitOp(self)




    def op(self):

        localctx = BayesGrammarParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.operator()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BayesGrammarParser.T__7:
                self.state = 54
                self.match(BayesGrammarParser.T__7)
                self.state = 55
                self.operator()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





