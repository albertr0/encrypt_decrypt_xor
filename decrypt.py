import sys


def citireDate():
    return sys.argv[1], sys.argv[2], sys.argv[3]


def charToBin(caracter):
    caracterInt = ord(caracter)
    l = []
    for i in range(8):
        l.append(str(int(caracterInt % 2)))
        caracterInt /= 2

    l.reverse()
    s = "".join(l)
    return s


def textToBin(sir):
    sir2 = ""
    for caracter in sir:
        sir2 = sir2+ charToBin(caracter)

    return sir2


def XorChr(ca1, ca2):
    c1 = int(ca1)
    c2 = int(ca2)
    c3 = c1 ^ c2

    return c3


def XorSiruri(sir, cheie):
    sir2 = ""
    for i in range(len(sir)):
        sir2 = sir2 + str(XorChr(sir[i], cheie[i]))

    return sir2

def sirinchr(sir):
    L = []
    i = 0
    while i < len(sir):
        L.append(sir[i])
        i = i + 1
        if ( i % 8 == 0 ) :
            numar = 0
            for j in range(0 , 8):
                numar = numar + int(L[j]) * 2 ** (7 - j)
            X.append(numar)
            L.clear()

          #############################################################################################################################################

inputFileName, cheie, outputFileName = citireDate()
fileInput = open(inputFileName)
text = fileInput.read()
fileInput.close()

textBinar = text
cheieBinar = textToBin(cheie)

cheieBinarMul = (len(textBinar) // len(cheieBinar) + 1) * cheieBinar
sirDecriptat = XorSiruri(textBinar, cheieBinarMul)

X = []
sirFinal = ""
sirinchr(sirDecriptat)
for i in X:
    sirFinal = sirFinal + chr(i)

fileOutput = open(outputFileName, 'wt', encoding='utf-8')
fileOutput.write(sirFinal)
fileOutput.close()
