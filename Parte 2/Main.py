from antlr4 import *
from BayesInput.BayesGrammarLexer import BayesGrammarLexer
from BayesInput.BayesGrammarParser import BayesGrammarParser
from MyCode import BayesListener
from BayesianNetwork import BayesianNetwork

from BayesUser.BayesGrammarUserLexer import BayesGrammarUserLexer
from BayesUser.BayesGrammarUserParser import BayesGrammarUserParser
from MyCode2 import BayesUserListener

gPath = raw_input("Ingrese el path del documento: ")
nFile = open(gPath,'r')
string=nFile.read()

nFile.close()

lexer = BayesGrammarLexer(InputStream(string))
stream = CommonTokenStream(lexer)
parser = BayesGrammarParser(stream)
tree = parser.program()
printer = BayesListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)

#print "probabilidades"
#for probability in printer.probabilities:
    #print probability
#print printer.variables

bn = BayesianNetwork(printer.probabilities, printer.variables)
if bn.hasError:
    print bn.error
else:
    print string
    try:
        while True:
            string = raw_input("Ingrese consulta: ")
            print "consulta "+string
            lexer = BayesGrammarUserLexer(InputStream(string))
            stream = CommonTokenStream(lexer)
            parser = BayesGrammarUserParser(stream)
            tree = parser.program()
            printer = BayesUserListener()
            walker = ParseTreeWalker()
            walker.walk(printer, tree)
            print bn.enumeration(printer.probability, printer.variables)
    except KeyboardInterrupt:
        print 'interrupted!'

    


