from random import shuffle
from os import remove
#prepare documents

def splitDocument(name,percent):
    f = open(name,'rb')
    lines = f.readlines()
    f.close()
    length = len(lines)
    nlines = []#cantidad de lineas a tomar
    for per in percent:#para cada probabilidad
        if len(nlines) == len(percent)-1:#quiere decir que ya solo falta 1
            nlines.append(length-sum(nlines))#le dejo lo que sobra
        else:
            nlines.append(int(length*per))
    
    #nlines tiene la cantidad de lineas para cada documento
    shuffle(lines)#se randomea el documento

    count = 0
    training = []
    cross = []
    test = []
    for line in lines:#para cada linea
        if count<nlines[0]:
            training.append(line)
        elif count < nlines[0]+nlines[1]:
            cross.append(line)
        else:
            test.append(line)
        count += 1
    
    try:
        remove('training'+name)
    except OSError:
        pass
    
    try:
        remove('cross'+name)
    except OSError:
        pass

    try:
        remove('test'+name)
    except OSError:
        pass

    f = open('training'+name,'w+')
    for line in training:
        f.write(line)
    f.close()
    f = open('cross'+name,'w+')
    for line in cross:
        f.write(line)
    f.close()
    f = open('test'+name,'w+')
    for line in test:
        f.write(line)
    f.close()


splitDocument('test_corpus.txt',[0.8,0.1,0.1])
