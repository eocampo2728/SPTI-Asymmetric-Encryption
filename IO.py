import os

def generateFile(texto, nameFile):
    with open(nameFile, 'wb') as f:
        f.write(texto)


def readText(textFile):
    f = open(textFile, 'rb')
    message = f.read()
    f.close()
    return message


