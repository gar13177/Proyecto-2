from texto import lectura, fromCountToProb, getProbFromPhrase
from decimal import Decimal as dec
from fractions import Fraction as frac
from scipy.optimize import minimize
from numpy import array
from os import remove

wordsP = None
nspamP = None
wordsC = None
spamWP = None

def getK():
    global wordsP, nspamP, wordsC, spamWP
    neg = {'ham':'!spam'}

    #obtengo la lectura de spam y palabras
    (spamP,spamWP, wordsC) = lectura('trainingtest_corpus.txt')
    #print spamP cantidad de palabras con spam
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
    print maximize(x0)
    #print minimize(maximize,x0, options={'maxiter':10})
    #print maximize(x0)
    #print eval(x0)
    while True:
        name = raw_input("Ingrese nombre del archivo a evaluar: ")
        tryeval(x0,name)
        print "Procesamiento terminado"


def maximize(x0):
    threshold = x0[1]
    k = int(x0[0])
    f = open('crosstest_corpus.txt','rb')
    lines = f.readlines()
    f.close()
    results = []
    for line in lines:
        val = line.split('\t')
        temp = getProbFromPhrase(val[1], wordsC, nspamP, spamWP, k)
        np = dec(temp.numerator)/dec(temp.denominator)
        if (np > threshold) and (val[0] == 'spam'):
            results.append(1)
        elif (np <= threshold) and (val[0] != 'spam'):
            results.append(1)
        else:
            results.append(0)
    return -1* sum(results)/float(len(results))

def eval(x0):
    threshold = x0[1]
    k = int(x0[0])
    f = open('testtest_corpus.txt','rb')
    lines = f.readlines()
    f.close()
    results = []
    for line in lines:
        val = line.split('\t')
        temp = getProbFromPhrase(val[1], wordsC, nspamP, spamWP, k)
        np = dec(temp.numerator)/dec(temp.denominator)
        if (np > threshold) and (val[0] == 'spam'):
            results.append(1)
        elif (np <= threshold) and (val[0] != 'spam'):
            results.append(1)
        else:
            results.append(0)
    return -1* sum(results)/float(len(results))

def tryeval(x0, name):
    threshold = x0[1]
    k = int(x0[0])

    try:
        remove('result'+name)
    except OSError:
        pass

    f = open(name,'rb')
    lines = f.readlines()
    f.close()
    f = open('result'+name,'w+')
    
    for line in lines:
        temp = getProbFromPhrase(line, wordsC, nspamP, spamWP, k)
        np = dec(temp.numerator)/dec(temp.denominator)
        if (np > threshold):
            f.write('spam\t'+line)
        else:
            f.write('ham\t'+line)
    f.close()

getK()
