import os

"""
    Method to save a text in a given file
    texto: Text to save
    nameFile: Name/path of file
"""
def generateFile(texto, nameFile):
    with open(nameFile, 'wb') as f:
        f.write(texto)
    print ("\nYour text were saved on "+nameFile)

"""
    Method that returns the text contained in a file
    textFile: File to read
"""
def readText(textFile):
    f = open(textFile, 'rb')
    message = f.read()
    f.close()
    return message


