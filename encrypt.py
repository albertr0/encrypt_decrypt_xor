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


          #############################################################################################################################################

cheie, inputFileName, outputFileName = citireDate()
fileInput = open(inputFileName, encoding="utf-8")
text = fileInput.read()
fileInput.close()

textBinar = textToBin(text)
cheieBinar = textToBin(cheie)

cheieBinarMul = (len(textBinar) // len(cheieBinar) + 1) * cheieBinar  #va fi mai lunga decat textBinar da nu cont deoarece parcurgem pana la len(textBinar)
sirCriptat = XorSiruri(textBinar, cheieBinarMul)

fileOutput = open(outputFileName, "w")
fileOutput.write(sirCriptat)
fileOutput.close()
