from collections import defaultdict
from decimal import Decimal as dec
from fractions import Fraction as frac

grb = ['\n','\t','\r','.',',',';']

def lectura(nombre):
    documento = open(nombre,'rb')

    wordsP = {}
    spamP = defaultdict(int)
    spamWP = defaultdict(int)

    for line in documento:
        nline = construccion(line)
        if nline != None:#si retorno un diccionario
            spamP[nline[0]] += 1
            spamWP[nline[0]] += sum(nline[1].values())
            for key in nline[1].keys():#recorro el diccionario
                if wordsP.has_key(key):
                    if wordsP[key].has_key(nline[0]):#si ya esta en spam o ham
                        wordsP[key][nline[0]] += nline[1][key]#agrego el valor al diccionario
                    else:
                        wordsP[key][nline[0]] = nline[1][key]
                else:
                    temp = {}
                    temp[nline[0]] = nline[1][key]
                    wordsP[key] = temp
    documento.close()
    #retorno 3 diccionarios:
    # 1. diccionario {spam, ham} con el conteo de cada uno
    # 2. diccionario {spam, ham} con el conteo de palabras en cada uno
    # 3. diccionario {word: {spam, ham}, ...} con el conteo de cada palabra
    return (spamP,spamWP, wordsP)

def fromLineToArray(line):
    line = clearString(line)


def construccion(line):
    val = line.split("\t")
    if len(val) == 2: #existe solo un \t
        words = clearString(val[1]).lower().split(' ') #obtengo el texto a analizar separado por espacios
        if '' in words:
            words.remove('')
        count = defaultdict(int)
        for word in words:
            count[word]+=1
        return (val[0],count) #retornamos probabilidad, diccionario
    return None

def fromCountToProb(wordsP, spamWP):#dicionario de palabras con el conteo
    prob = {}
    neg = {'ham':'!spam'}
    for word in wordsP.keys():
        temp = {}
        for key in wordsP[word].keys():
            p = frac(wordsP[word][key],spamWP[key])
            if key in neg.keys():
                key = neg[key]
            temp[key] = p
        prob[word] = temp
    return prob#construye  un diccionario de probabilidades

#wordsP dictionary
#P(word|depen) return
def getProb(wordsP, word,spamP, depen,k):
    if depen == '!spam': depen = 'ham'
    if word in wordsP.keys():
         if depen in wordsP[word].keys():
             return frac(wordsP[word][depen]+k,spamP[depen]+2*k)#deberia ser la cantidad de palabras 
    return frac(0+k,spamP[depen]+2*k)

#probabilidad de frase:
#phrase es la frase 
#wordsP es la cantidad de palabras en spam o ham
#spamP es la probabilidad 0.0 de ocurrencia
#spamC es la cantidad de palabras por spamC
#k 
def getProbFromPhrase(phrase, wordsP, spamP,spamC, k):
    phrase = clearString(phrase)
    words = phrase.lower().split(' ')
    if '' in words:
        words.remove('')
    probS = spamP['spam']
    probH = spamP['!spam']
    for word in words:
        probS = probS * getProb(wordsP, word,spamC, 'spam', k)
        probH = probH * getProb(wordsP, word,spamC, '!spam', k)
    
    return frac(probS,probS+probH)

def clearString(string):
    for char in grb:
        string = string.replace(char,'')
    return string
