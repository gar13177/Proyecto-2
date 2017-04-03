from BayesUser.BayesGrammarUserListener import BayesGrammarUserListener

class BayesUserListener(BayesGrammarUserListener):
    variables = []
    probability = []

    def enterProgram(self, ctx):
        self.variables = []
        self.probability = []
        self.probability = self.enterProbability(ctx.probability())

    def enterProbability(self, ctx):
        condition = []
        for op in ctx.op():
            condition.append(self.enterOp(op))
        return condition

    def enterOperator(self, ctx):
        if ctx.TOKEN().getText() not in self.variables:
            self.variables.append(ctx.TOKEN().getText())
        if ctx.negation() != None:
            return (-1,ctx.TOKEN().getText())
        else:
            return (1,ctx.TOKEN().getText())
    
    def enterOp(self, ctx):
        tokens = []
        for operator in ctx.operator():
            tokens.append(self.enterOperator(operator))
        return tokens
        

