from texto import lectura, fromCountToProb, getProbFromPhrase
from decimal import Decimal as dec
from fractions import Fraction as frac
from scipy.optimize import minimize
from numpy import array

wordsP = None
nspamP = None

def getK():
    global wordsP, nspamP
    neg = {'ham':'!spam'}

    #obtengo la lectura de spam y palabras
    (spamP,spamWP, wordsC) = lectura('testtest_corpus.txt')
    total = sum(spamP.values())
    nspamP = {}
    for key in spamP.keys():
        p = frac(spamP[key],total)
        if key in neg.keys():
            key = neg[key]
        nspamP[key] = p
    #probabilidad 0.0...
    wordsP = fromCountToProb(wordsC, spamWP)
    x0 = array([1, 0.5])
    print minimize(maximize,x0)


def maximize(x0):
    threshold = x0[1]
    k = x0[0]
    f = open('crosstest_corpus.txt','rb')
    lines = f.readlines()
    f.close()
    results = []
    for line in lines:
        val = line.split('\t')
        temp = getProbFromPhrase(val[1], wordsP, nspamP, k)
        np = dec(temp.numerator)/dec(temp.denominator)
        if (np > threshold) and (val[0] == 'spam'):
            results.append(1)
        elif (np <= threshold) and (val[0] != 'spam'):
            results.append(1)
        else:
            results.append(0)
    return -1* sum(results)/float(len(results))

getK()
