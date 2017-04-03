from copy import deepcopy

class BayesianNetwork ():
    probabilities = []#probailidades recibidas por el parser
    variables = []#todas las posibles variables
    dictionary = {}#jerarquia de dependencias
    bProbabilities = {}#probabilidades construidas correctamente

    error = ""
    hasError = False

    def __init__(self, probabilities, variables):
        self.probabilities = probabilities
        self.variables = variables
        dictionary = {}
        for variable in variables:
            dictionary[variable] = []
        self.dictionary = dictionary
        self.build()
        self.buildTables()

    def build(self):
        #formato de la probabilidad:
        #[[[a,b,c],|[d,e,f]],P]
        for probability in self.probabilities:#empezamos con las dependencias
            if len(probability[0]) > 1:#quire decir que hay una condicion
                for element in probability[0][0]:
                    for dependent in probability[0][1]:
                        if dependent[1] not in self.dictionary.get(element[1]):
                            self.dictionary.get(element[1]).append(dependent[1])
        #ya tengo el diccionario

        

    def buildTables(self):
        dictionary = {}
        for key, value in self.dictionary.iteritems():
            dictionary[key] = self.buildProbabilty(key,value)
        self.bProbabilities = dictionary
        
            
    
    def buildProbabilty(self, key, value):
        exp = len(value)
        expected = 2**exp
        comb = []

        #primero coloco las dos posibilidades para el key
        comb.append([(1,key)])
        comb.append([(-1,key)])

        for element in value:
            temp1 = deepcopy(comb)
            temp2 = deepcopy(comb)
            
            for pr in temp1:
                pr.append((1,element))
            
            for pr in temp2:
                pr.append((-1,element))
            
            #comb = deepcopy([])
            comb = temp1[:]+temp2[:]
        
        probailities = []
        for element in comb:
            temp = self.searchProbability(element)
            if len(temp) == 0:
                self.hasError = True
                self.error = "No descrito completamente\nFalla con "+str(element)
            else:
                probailities.append(temp)
        return probailities

    def searchProbability(self, element):
        #element = [(1, u'F'), (1, u'S'), (1, u'A')]
        #donde esta asi: F | S, A 
        for probability in self.probabilities:
            if (probability[0][0][0][1] == element[0][1]):
                if len(element) > 1:
                    flag = True#asumo que si esta
                    for i in range(1,len(element)):#busco desde el 2
                        if element[i] not in probability[0][1]:
                            flag = False#ya se que no es esta la combinacion
                    if flag:#quiere decir que si esta aqui
                        if (element[0][0] == probability[0][0][0][0]):
                            return (element, probability[1])
                        else:
                            return (element, 1-probability[1])
                else:
                    if len(probability[0]) == 1:
                        if (element[0][0] == probability[0][0][0][0]):
                            return (element, probability[1])
                        else:
                            return (element, 1-probability[1])
        return ()

    def enumeration(self, probability, variables):
        #probability es como lo da el parser [[[]]]
        #variables es un diccionario
        print "probability "+str(probability)
        print "vvariables "+str(variables)
        
        for variable in variables:
            if variable not in self.variables:
                return "Variable: "+str(variable)+" no definida"

        temp = probability[0]
        if len(probability) > 1:
            temp = probability[0]+probability[1]
        #print "numerador: "+str(temp)
        num1 = self.getProbability(temp, variables)
        #ya tengo las que no estan no_incluidas
        num2 = 1.0
        if len(probability) > 1:
            #print "probabilidad 2"
            v1 = []
            for element in probability[1]:
                if element[1] not in v1:
                    v1.append(element[1])
            num2 = self.getProbability(probability[1],v1)
        return str(num1/num2)

    def getProbability(self, probability, v1):
        """recibe el vector de probabilidad con las variables incluidas en esa probailidad"""

        notIncluded = []
        for variable in self.variables:
            if variable not in v1:
                notIncluded.append(variable)

        if len(notIncluded)==0:#quiere decir que tiene todas las variables
            #print "tiene todas las variables "+str(probability)
            return self.computeProbability(probability)

        comb = []
        for element in notIncluded:
            if len(comb) == 0:
                comb.append([(1, element)])
                comb.append([(-1, element)])
            else:
                temp1 = deepcopy(comb)
                temp2 = deepcopy(comb)
                
                for pr in temp1:
                    pr.append((1, element))
                
                for pr in temp2:
                    pr.append((-1, element))

                #comb = deepcopy([])
                comb = temp1[:]+temp2[:]
        
        for element in probability:
            for elementc in comb:
                elementc.append(element)
        
        val = 0
        for element in comb:
            val += self.computeProbability(element)
        
        return val
        
    def computeProbability(self, comb):
        """recibe la combinacion del cual se calculara la probabilidad conjunta"""
        
        val = 1
        for key, value in self.bProbabilities.iteritems():
            #value es un vector de tublas ([(!,A)], 0.5)
            for tup in value:#value es un vector que tiene P(a), valor
                flag = True#supongo que si lo voy a encontrar
                for p in tup[0]:#p = (1,A)
                    if p not in comb:
                        flag = False
                if flag:#quiere decir que si estaba adentro
                    #print "se multiplica: "+str(tup[0])+" val: "+str(tup[1])
                    val = val * tup[1]#lo multiplico por el valor de esa combinacion
            
        return val

    def printFactores(self):
        expr = ""
        
        for k, v in self.bProbabilities.items():
            for element in v:
                k = 0
                for element2 in element[0]:
                    if k == 0:
                        expr += "p("
                        if element2[0] == 1:
                            expr+=str(element2[1])#+")"
                        else:
                            expr+="!"+str(element2[1])#+")"
                    elif k == 1:
                        expr +="|"
                        if element2[0] == 1:
                            expr+=str(element2[1])#+")"
                        else:
                            expr+="!"+str(element2[1])#+")"
                    else:
                        expr +=","
                        if element2[0] == 1:
                            expr+=str(element2[1])#+")"
                        else:
                            expr+="!"+str(element2[1])#+")"
                        
                    k+= 1
                        
                expr +=") = "+str(element[1])+"\n"
                        
        print expr

        comp = ""

        for k, v in self.dictionary.items():
            if len(v)==0:
                comp += "p("+str(k)+")"
            else:
                comp += "p("+str(k)+"|"
                k = 0
                for element in v:
                    if k == 0:
                        comp+=str(element)
                    else:
                        comp+=","+str(element)
                    k+= 1
                comp+=")"
        print comp

        

    def getDigraph(self):
        print self.dictionary
        edge = []
        path = []
        
        for k, v in self.dictionary.items():
            if len(v)==0:
                edge.append(k)
            else:
                for element in v:
                    path.append((element,k))
        return (edge,path)
        

                


