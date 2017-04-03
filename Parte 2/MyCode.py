from BayesInput.BayesGrammarListener import BayesGrammarListener

class BayesListener(BayesGrammarListener):
    variables = []
    probabilities = []

    def enterProgram(self, ctx):
        self.variables = []
        self.probabilities = []
        probabilities = []
        for pr in ctx.probability():
            probabilities.append(self.enterProbability(pr))
        self.probabilities = probabilities

    def enterProbability(self, ctx):
        probability = []
        condition = []
        for op in ctx.op():
            condition.append(self.enterOp(op))
        probability.append(condition)
        probability.append(self.enterNumber(ctx.number()))
        return probability


    def enterNumber(self, ctx):
        print ctx
        return float(ctx.getText())

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
        

