# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
import sys


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

def readFromSys():
    nombrearch=tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    if nombrearch!='':
        """Aquí tenemos la variable del archivo"""
        archi1=open(nombrearch, "rb")
        contenido=archi1.read()
        archi1.close()
        print(contenido)
        return contenido
    return ""






